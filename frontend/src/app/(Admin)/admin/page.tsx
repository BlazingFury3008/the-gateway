"use client";
import { useState, useEffect } from "react";
import api from "@/lib/axios";
import Papa from "papaparse";

export default function AdminPage() {
  const [tables, setTables] = useState<string[]>([]);
  const [selectedTable, setSelectedTable] = useState<string | null>(null);
  const [tableData, setTableData] = useState<any[]>([]);
  const [columnTypes, setColumnTypes] = useState<{ [key: string]: string }>({});
  const [newTableName, setNewTableName] = useState("");
  const [columns, setColumns] = useState<{ name: string; type: string }[]>([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [csvFile, setCsvFile] = useState<File | null>(null);

  // SQL Data Types with Sub-Options
  const dataTypes = {
    Numeric: ["INT", "FLOAT", "DOUBLE", "DECIMAL"],
    String: ["VARCHAR", "TEXT", "TINYTEXT", "MEDIUMTEXT", "LONGTEXT"],
    DateTime: ["DATE", "DATETIME", "TIMESTAMP"],
    Boolean: ["BOOLEAN"],
  };

  useEffect(() => {
    fetchTables();
  }, []);

  const fetchTables = async () => {
    try {
      const response = await api.get("/tables");
      setTables(response.data.tables);
      if (response.data.tables.length > 0) {
        fetchTableData(response.data.tables[0]);
      }
    } catch (error) {
      console.error("Error fetching tables:", error);
    }
  };

  const createTable = async () => {
    if (!newTableName.trim() || columns.length === 0) return;
    try {
      const formattedColumns = columns.reduce((acc, col) => {
        acc[col.name] = col.type;
        return acc;
      }, {} as Record<string, string>);

      await api.post("/tables", {
        table_name: newTableName,
        columns: formattedColumns,
      });

      setNewTableName("");
      setColumns([]);
      fetchTables();
      setModalOpen(false);
    } catch (error) {
      console.error("Error creating table:", error);
    }
  };

  const fetchTableData = async (tableName: string) => {
    setSelectedTable(tableName);
    try {
      const response = await api.get(`/tables/${tableName}`);
      setTableData(response.data.data || []);
      setColumnTypes(response.data.column_types || {});
    } catch (error) {
      console.error("Error fetching table data:", error);
    }
  };

  // Handle CSV Upload
  const handleCsvUpload = async () => {
    if (!csvFile) return;
    Papa.parse(csvFile, {
      header: true,
      skipEmptyLines: true,
      complete: async function (results) {
        if (!results.data || results.data.length === 0) return;
        const csvColumns = Object.keys(results.data[0]);

        // Guess column types
        const detectedColumns = csvColumns.map((col) => ({
          name: col,
          type: "VARCHAR(255)", // Default to VARCHAR
        }));

        // Send data to backend for table creation
        try {
          const formattedColumns = detectedColumns.reduce((acc, col) => {
            acc[col.name] = col.type;
            return acc;
          }, {} as Record<string, string>);

          await api.post("/tables", {
            table_name: csvFile.name.replace(".csv", ""),
            columns: formattedColumns,
          });

          // Insert CSV data into the new table
          await api.post(`/tables/${csvFile.name.replace(".csv", "")}/insert-bulk`, {
            data: results.data,
          });

          setCsvFile(null);
          fetchTables();
        } catch (error) {
          console.error("Error importing CSV:", error);
        }
      },
    });
  };

  return (
    <div className="p-6 min-h-screen bg-[var(--color-background)]">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-[var(--color-foreground)]">Database Admin</h1>
      </div>

      <div className="grid grid-cols-4 gap-6">
        {/* Sidebar */}
        <div className="p-6 rounded-lg shadow-lg bg-[var(--color-background-soft)] border border-[var(--color-border)]">
          <h2 className="text-lg font-semibold mb-4">Tables</h2>
          {tables.length > 0 ? (
            tables.map((table) => (
              <button
                key={table}
                className={`block w-full px-4 py-2 rounded-lg text-left mb-2 transition ${
                  selectedTable === table
                    ? "bg-[var(--color-primary)] text-white"
                    : "bg-[var(--color-background-hover)] hover:bg-[var(--color-secondary)] hover:text-white"
                }`}
                onClick={() => fetchTableData(table)}
              >
                {table}
              </button>
            ))
          ) : (
            <p className="text-gray-500">No tables found</p>
          )}
          <button onClick={() => setModalOpen(true)} className="btn btn-primary w-full mt-4">
            + Add Table
          </button>

          {/* CSV Import */}
          <div className="mt-6">
            <h3 className="text-lg font-semibold mb-2">Import CSV</h3>
            <input
              type="file"
              accept=".csv"
              onChange={(e) => setCsvFile(e.target.files?.[0] || null)}
              className="input mb-2"
            />
            <button onClick={handleCsvUpload} className="btn btn-secondary w-full">
              Upload CSV
            </button>
          </div>
        </div>

        {/* Table Data */}
        <div className="col-span-3 p-6 rounded-lg shadow-lg bg-[var(--color-background)] border border-[var(--color-border)]">
          <h2 className="text-xl font-bold mb-4 text-[var(--color-foreground)]">
            {selectedTable ? `Table: ${selectedTable}` : "Select a table"}
          </h2>
          {selectedTable && tableData.length > 0 ? (
            <div className="overflow-x-auto">
              <table className="w-full border-collapse border border-[var(--color-border)]">
                <thead>
                  <tr className="bg-[var(--color-background-soft)] text-[var(--color-foreground)]">
                    {Object.keys(tableData[0]).map((col) => (
                      <th key={col} className="border border-[var(--color-border)] p-3 text-left">
                        {col}<br />
                        <span className="text-xs text-[var(--color-foreground-soft)]">
                          ({columnTypes[col] ? columnTypes[col] : "UNKNOWN"})
                        </span>
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {tableData.map((row, index) => (
                    <tr key={index} className="border border-[var(--color-border)]">
                      {Object.entries(row).map(([col, value]) => (
                        <td key={col} className="border border-[var(--color-border)] p-2">
                          {String(value)}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <p className="text-gray-500">No data available</p>
          )}
        </div>
      </div>
       {/* Modal for Creating New Table */}
       {modalOpen && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
            <div className="p-6 rounded-lg shadow-lg bg-[var(--color-background)] border border-[var(--color-border)] md:w-[1000px] w-11/12">
              <h2 className="text-lg font-bold mb-4">Create Table</h2>
              <input
                type="text"
                value={newTableName}
                onChange={(e) => setNewTableName(e.target.value)}
                placeholder="Table name"
                className="input mb-4"
              />

              <h3 className="text-lg font-semibold mb-2">Columns</h3>
              {columns.map((col, index) => (
                <div key={index} className="flex space-y-2">
                  <div className="flex mb-4 w-full space-x-2">
                  <input
                    type="text"
                    placeholder="Column Name"
                    value={col.name}
                    onChange={(e) => {
                      const updatedCols = [...columns];
                      updatedCols[index].name = e.target.value;
                      setColumns(updatedCols);
                    }}
                    className="input"
                  />
                  <select
                    value={col.type}
                    onChange={(e) => {
                      const updatedCols = [...columns];
                      updatedCols[index].type = e.target.value;
                      setColumns(updatedCols);
                    }}
                    className="w-4/12 input"
                  >
                    {Object.entries(dataTypes).map(([category, types]) => (
                      <optgroup key={category} label={category}>
                        {types.map((type) => (
                          <option key={type} value={type}>
                            {type}
                          </option>
                        ))}
                      </optgroup>
                    ))}
                  </select>
                  </div>
                  <input type="button" value="X" onClick={() => {
                    setColumns(columns.filter((val, i) => i != index))
                  }}/>
                  <div>

                  </div>
                </div>
              ))}
              <button onClick={() => setColumns([...columns, { name: "", type: "VARCHAR(255)" }])} className="btn btn-secondary mb-4">
                + Add Column
              </button>

              <div className="flex justify-end space-x-2">
                <button onClick={() => setModalOpen(false)} className="btn btn-danger">
                  Cancel
                </button>
                <button onClick={createTable} className="btn btn-primary">
                  Create
                </button>
              </div>
            </div>
          </div>
        )}
    </div>
  );
}
