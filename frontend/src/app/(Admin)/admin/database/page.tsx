"use client";

import { excludedTables } from "@/components/admin/menu";
import api from "@/lib/axios";
import Link from "next/link";
import { useSearchParams, useRouter } from "next/navigation";
import React, { useEffect, useState } from "react";

export default function Page() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const table = searchParams.get("table");

  const [tableData, setTableData] = useState<{ table: string; data: number | null }[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState("");

  const [selectedTableData, setSelectedTableData] = useState<any[]>([]);
  const [selectedTableLoading, setSelectedTableLoading] = useState(false);
  const [selectedTableError, setSelectedTableError] = useState<string | null>(null);
  const [tableSearchQuery, setTableSearchQuery] = useState("");
  const [selectedColumn, setSelectedColumn] = useState<string>("");

  useEffect(() => {
    const fetchTables = async () => {
      try {
        const res = await api.get("/tables");
        const tables: string[] = res.data.tables.filter((t: string) => !excludedTables.includes(t));

        const data = await Promise.all(
          tables.map(async (table) => {
            try {
              const tableRes = await api.get(`data/${table}`);
              return { table, data: tableRes.data.length };
            } catch {
              return { table, data: null };
            }
          })
        );

        setTableData(data);
      } catch (error) {
        console.error("Error fetching tables:", error);
        setError("Failed to load tables.");
      } finally {
        setLoading(false);
      }
    };

    if (!table) {
      fetchTables();
    }
  }, [table]);

  // Fetch specific table data when table is selected
  useEffect(() => {
    if (!table) return;

    const fetchTableData = async () => {
      setSelectedTableLoading(true);
      setSelectedTableError(null);
      try {
        const res = await api.get(`data/${table}`);
        setSelectedTableData(res.data);
      } catch (error) {
        console.error(`Error fetching data for ${table}:`, error);
        setSelectedTableError(`Failed to load data for ${table}`);
      } finally {
        setSelectedTableLoading(false);
      }
    };

    fetchTableData();
  }, [table]);

  const filteredTables = tableData.filter((t) =>
    t.table.toLowerCase().includes(searchQuery.toLowerCase())
  );

  // **🔍 Filter Table Data by Search Query & Column**
  const filteredTableData = selectedTableData.filter((row) => {
    if (!tableSearchQuery) return true;
    if (selectedColumn) {
      return String(row[selectedColumn]).toLowerCase().includes(tableSearchQuery.toLowerCase());
    }
    return Object.values(row).some((val) =>
      String(val).toLowerCase().includes(tableSearchQuery.toLowerCase())
    );
  });

  return (
    <div className="p-4">
      <h1 className="text-3xl font-bold mb-4 text-center">Database Tables</h1>

      {/* Search Bar for Table List */}
      {!table && (
        <div className="flex justify-center mb-4">
          <input
            type="text"
            placeholder="Search tables..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="input w-1/2"
          />
        </div>
      )}

      {/* If table is selected, show its data */}
      {table ? (
        <div>
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-2xl font-semibold">Table: {table}</h2>
            <button
              className="btn btn-primary"
              onClick={() => router.push("/admin/database")}
            >
              Back to All Tables
            </button>
          </div>

          {/* Search & Filter Section */}
          <div className="flex justify-center gap-4 mb-4">
            {/* Column Dropdown */}
            {selectedTableData.length > 0 && (
              <select
                className="input w-1/4"
                value={selectedColumn}
                onChange={(e) => setSelectedColumn(e.target.value)}
              >
                <option value="">All Columns</option>
                {Object.keys(selectedTableData[0]).map((col) => (
                  <option key={col} value={col}>
                    {col}
                  </option>
                ))}
              </select>
            )}

            {/* Search Input for Table Data */}
            <input
              type="text"
              placeholder="Search table data..."
              value={tableSearchQuery}
              onChange={(e) => setTableSearchQuery(e.target.value)}
              className="input w-1/2"
            />
          </div>

          {selectedTableLoading ? (
            <p className="text-center">Loading table data...</p>
          ) : selectedTableError ? (
            <p className="text-red-500 text-center">{selectedTableError}</p>
          ) : filteredTableData.length > 0 ? (
            <div className="overflow-x-auto">
              <table className="border-collapse border w-full mx-auto text-center border-[var(--color-border)]">
                <thead>
                  <tr className="bg-[var(--color-background-soft)] text-[var(--color-foreground)] font-bold">
                    {Object.keys(filteredTableData[0]).map((col) => (
                      <th key={col} className="border border-[var(--color-border)] p-3">
                        {col}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {filteredTableData.map((row, i) => (
                    <tr key={i} className="text-[var(--color-foreground)]">
                      {Object.values(row).map((val, j) => (
                        <td key={j} className="border border-[var(--color-border)] px-3 py-2">
                          {typeof val === "object" ? JSON.stringify(val) : val}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <p className="text-center">No matching data found.</p>
          )}
        </div>
      ) : (
        /* Display all tables */
        <>
          {loading ? (
            <p className="text-center">Loading...</p>
          ) : error ? (
            <p className="text-danger text-center">{error}</p>
          ) : filteredTables.length > 0 ? (
            <div className="overflow-x-auto">
              <table className="border-collapse border w-5/6 mx-auto text-center border-[var(--color-border)]">
                <thead>
                  <tr className="bg-[var(--color-background-soft)] text-[var(--color-foreground)] font-bold text-lg">
                    <th className="border border-[var(--color-border)] p-3">Table Name</th>
                    <th className="border border-[var(--color-border)] p-3">Entry Count</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredTables.map(({ table, data }) => (
                    <tr key={table} className="text-[var(--color-foreground)]">
                      <td className="border border-[var(--color-border)] px-3 py-2">
                        <Link href={`/admin/database?table=${table}`} className="text-blue-600 underline" onClick={() => {
                          setTableSearchQuery("");
                          setSelectedColumn("")
                        }}>
                          {table}
                        </Link>
                      </td>
                      <td className="border border-[var(--color-border)] px-3 py-2">
                        {data !== null ? data : "Error fetching data"}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <p className="text-center">No tables found.</p>
          )}
        </>
      )}
    </div>
  );
}
