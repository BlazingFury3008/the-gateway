import Link from "next/link";
import React from "react";
import { menu, MenuOption } from "./menu";



function SidebarSelection({ name, href, options, headerLevel }: MenuOption) {
  const padding = (() => {
    switch (headerLevel) {
      case "H1":
        return "";
      case "H2":
        return "px-1";
      case "H3":
        return "px-2";
      case "H4":
        return "px-3";
      default:
        return "px-4";
    }
  })();

  return (
    <div className={padding}>
      <Link href={`/admin${href}`} className={`hover:underline ${padding}`}>
        {name}
      </Link>
      {options?.map((x : MenuOption) => (
        <SidebarSelection {...x} key={x.href} />
      ))}
    </div>
  );
}

export default function Sidebar({
  databaseTables,
}: {
  databaseTables: string[];
}) {
  return (
    <div className="p-2">
      <h1 className="text-2xl">Admin</h1>
      {menu.map((menuItem) => (
        <SidebarSelection {...menuItem} key={menuItem.href} />
      ))}
      <SidebarSelection
        name={"Databases"}
        href={"/database"}
        headerLevel={"H1"}
      />
      {databaseTables.map((database, key) => (
        <SidebarSelection
        key={key}
          name={database}
          href={"/database?table=" + database}
          headerLevel={"H2"}
        />
      ))}
    </div>
  );
}
