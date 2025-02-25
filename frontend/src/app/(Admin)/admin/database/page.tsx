"use client";

import { excludedTables } from "@/components/admin/menu";
import api from "@/lib/axios";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import React, { useEffect, useState } from "react";

export default function Page() {
  const searchParams = useSearchParams();
  const table = searchParams.get("table");

  const [tableData, setTableData] = useState<{ table: string; data: any }[]>(
    []
  );

  useEffect(() => {
    const fetchTables = async () => {
      try {
        const res = await api.get("/tables");
        const tables: string[] = res.data.tables.filter((t : string) => !excludedTables.includes(t));

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

        if(data == null)
        {
            setTableData([])
        }
        else
        {
            setTableData(data);
        }
      } catch (error) {
        console.error("Error fetching tables:", error);
      }
    };

    if (!table) {
      fetchTables();
    }
  }, [table]); // Re-run when `table` changes

  if (table) {
    return <div>Table: {table}</div>;
  }

  return (
    <div className="p-2">
      <h2 className="text-3xl mb-3">All Tables</h2>
      {tableData.length > 0  ? (
  <table className="w-3/4 border-collapse border mx-8 text-left rounded-lg">
  {/* Table Header */}
  <thead className="border">
    <tr>
      <th className="px-2 border">Name</th>
      <th className="px-2 border">Entry Count</th>
    </tr>
  </thead>

  {/* Table Body */}
  <tbody className="">
    {tableData.map(({ table, data }) => (
      <tr key={table} className="hover:bg-gray-900 cursor-pointer transition duration-150 border">
        <td className="px-2 border">
          <Link href={"/admin/database?table="+table} className="text-blue-600 underline">
            {table}
          </Link>
        </td>
        <td className="px-2 border">{JSON.stringify(data, null, 2)}</td>
      </tr>
    ))}
  </tbody>
</table>
      ) : (
       <div>
         {table != null ?
                    <p>Loading...</p> : 
                    <p>No Tables Available</p>
        }
       </div>
      )}
    </div>
  );
}
