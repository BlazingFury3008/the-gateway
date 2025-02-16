"use client";
import { useState, useEffect } from "react";
import api from "@/lib/axios";
import { IoClose } from "react-icons/io5";
import { FaSpinner } from "react-icons/fa";

export default function AdminPage() {
  const [tables, setTables] = useState<string[]>([]);
  const [selectedTable, setSelectedTable] = useState<string | null>(null);
  const [tableData, setTableData] = useState<any[]>([]);
  const [columnTypes, setColumnTypes] = useState<{ [key: string]: string }>({});
  const [newRows, setNewRows] = useState<{ [key: string]: string | number }[]>(
    []
  );
  const [addRowModalOpen, setAddRowModalOpen] = useState(false);
  const [loading, setLoading] = useState(false); // Loading state for table switching

  // Hardcoded tables that cannot have data added or updated
  const readOnlyTables = ["system_logs", "audit_trail", "users"];

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

  const fetchTableData = async (tableName: string) => {
    setSelectedTable(tableName);
    setLoading(true);
    setTableData([]); // Clear table data while loading
    try {
      const response = await api.get(`/tables/${tableName}`);
      setTableData(response.data.data || []);
      setColumnTypes(response.data.column_types || {});
    } catch (error) {
      console.error("Error fetching table data:", error);
    } finally {
      setLoading(false);
    }
  };

  const addRows = async () => {
    if (
      !selectedTable ||
      newRows.length === 0 ||
      readOnlyTables.includes(selectedTable)
    )
      return;
    try {
      for (const row of newRows) {
        await api.post(`/tables/${selectedTable}/insert`, row);
      }
      fetchTableData(selectedTable);
      setNewRows([]);
      setAddRowModalOpen(false);
    } catch (error) {
      console.error("Error adding rows:", error);
    }
  };

  const addNewRow = () => {
    if (!selectedTable || readOnlyTables.includes(selectedTable)) return;
    const emptyRow = Object.keys(columnTypes).reduce((acc, key) => {
      acc[key] = "";
      return acc;
    }, {} as { [key: string]: string | number });
    setNewRows([...newRows, emptyRow]);
  };

  const deleteRow = async (rowData: any) => {
    if (!selectedTable) return;
    try {
      const primaryKey = Object.keys(rowData)[0];
      await api.delete(`/tables/${selectedTable}/delete`, {
        data: { conditions: { [primaryKey]: rowData[primaryKey] } },
      });
      fetchTableData(selectedTable);
    } catch (error) {
      console.error("Error deleting row:", error);
    }
  };

  return (
    <div
      className={`p-6 min-h-screen bg-[var(--color-background-soft)]`}
    >
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-[var(--color-foreground)]">
          Database Admin
        </h1>
      </div>

      <div className="grid grid-cols-6 gap-6">
        {/* Sidebar for Tables */}
        <div className="p-6 rounded-lg shadow-lg bg-[var(--color-form)] border border-[var(--color-border)]">
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
                onClick={() => {
                  setTableData([]);
                  fetchTableData(table);
                }}
              >
                {table} {readOnlyTables.includes(table) && "(Read-Only)"}
              </button>
            ))
          ) : (
            <p className="text-gray-500">No tables found</p>
          )}
        </div>

        {/* Table Data */}
        <div className="col-span-5 p-6 rounded-lg shadow-lg bg-[var(--color-form)] border border-[var(--color-border)]">
          <h2 className="text-xl font-bold mb-4 text-[var(--color-foreground)]">
            {selectedTable ? `Table: ${selectedTable}` : "Select a table"}
          </h2>

          {/* Loading Spinner */}
          {loading ? (
            <div className="flex justify-center items-center py-10">
              <FaSpinner className="animate-spin text-4xl text-[var(--color-primary)]" />
            </div>
          ) : selectedTable && tableData.length > 0 ? (
            <>
              <div className="overflow-x-auto">
                <table className="w-full border-collapse border border-[var(--color-border)] rounded-">
                  <thead>
                    <tr className="bg-[var(--color-background-soft)] text-[var(--color-foreground)]">
                      {Object.keys(tableData[0]).map((col) => (
                        <th
                          key={col}
                          className="border border-[var(--color-border)] p-3 text-left"
                        >
                          {col}
                        </th>
                      ))}
                      <th className="border border-[var(--color-border)] p-3">
                        Actions
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    {tableData.map((row, index) => (
                      <tr
                        key={index}
                        className="border border-[var(--color-border)]"
                      >
                        {Object.entries(row).map(([col, value]) => (
                          <td
                            key={col}
                            className="border border-[var(--color-border)] p-2"
                          >
                            {String(value)}
                          </td>
                        ))}
                        <td className="border border-[var(--color-border)] p-2">
                          <button
                            onClick={() => deleteRow(row)}
                            className="bg-red-500 text-white px-2 py-1 rounded"
                          >
                            Delete
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </>
          ) : (
            <p className="text-gray-500">No data available</p>
          )}
          {/* Open Add Row Modal (Only if not read-only) */}
          {!readOnlyTables.includes(selectedTable) && (
            <button
              onClick={() => setAddRowModalOpen(true)}
              className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
            >
              + Add Row
            </button>
          )}
          {/* Add Row Modal */}
          {addRowModalOpen && (
  <div className="fixed inset-0 bg-[var(--color-shadow)] flex justify-center items-center px-4">
    <div className="bg-[var(--color-background)] dark:bg-[var(--color-background-hover)] p-6 rounded-lg shadow-lg w-full max-w-2xl relative border border-[var(--color-border)]">
      
      {/* Close Button */}
      <button
        onClick={() => setAddRowModalOpen(false)}
        className="absolute top-3 right-3 text-[var(--color-foreground-soft)] dark:text-[var(--color-foreground-hover)] hover:text-[var(--color-danger)] transition"
      >
        <IoClose size={28} />
      </button>

      {/* Modal Header */}
      <h3 className="text-xl font-semibold mb-4 text-[var(--color-foreground)] dark:text-[var(--color-foreground-hover)] text-center">
        Add New Rows
      </h3>

      {/* Row Input Fields */}
      <div className="space-y-4 max-h-80 overflow-y-auto p-2 border rounded-lg bg-[var(--color-background-soft)]">
        {newRows.length === 0 ? (
          <p className="text-center text-[var(--color-foreground-soft)]">
            No rows added. Click below to add rows.
          </p>
        ) : (
          newRows.map((row, index) => (
            <div key={index} className="flex flex-wrap gap-2 items-center border p-3 rounded-lg bg-[var(--color-background)]">
              {Object.keys(columnTypes).map((col) => (
                <input
                  key={col}
                  type="text"
                  placeholder={col}
                  className="p-2 border rounded w-full sm:w-1/2 bg-[var(--color-form)] text-[var(--color-foreground)] focus:outline-none focus:ring-2 focus:ring-[var(--color-primary-hover)]"
                  value={row[col] || ""}
                  onChange={(e) => {
                    const updatedRows = [...newRows];
                    updatedRows[index][col] = e.target.value;
                    setNewRows(updatedRows);
                  }}
                />
              ))}
              {/* Remove Row Button */}
              <button
                onClick={() => setNewRows(newRows.filter((_, i) => i !== index))}
                className="text-[var(--color-danger)] hover:text-[var(--color-primary-hover)] transition ml-auto"
              >
                <IoClose size={20} />
              </button>
            </div>
          ))
        )}
      </div>

      {/* Modal Footer */}
      <div className="flex justify-between items-center mt-4">
        <button
          onClick={addNewRow}
          className="px-4 py-2 bg-[var(--color-background-hover)] dark:bg-[var(--color-primary)] text-[var(--color-foreground)] rounded-lg hover:bg-[var(--color-primary-hover)] transition"
        >
          + Add Another Row
        </button>
        <button
          onClick={addRows}
          className="px-4 py-2 bg-[var(--color-primary)] text-white rounded-lg hover:bg-[var(--color-primary-hover)] transition"
          disabled={newRows.length === 0}
        >
          Submit Rows
        </button>
      </div>
    </div>
  </div>
)}

        </div>
      </div>
    </div>
  );
}
