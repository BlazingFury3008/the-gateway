export interface MenuOption {
    name: string;
    href: string;
    headerLevel: "H1" | "H2" | "H3" | "H4" | "H5";
    options?: MenuOption[];
  }
  
export const menu: MenuOption[] = [
    {
        name: "Home",
        href: "/",
        headerLevel: "H1"
      },
      {
        name: "API Keys",
        href: "/api-keys",
        headerLevel: "H1"
      },
      {
        name: "Users",
        href: "/users",
        headerLevel: "H1",
      },
      {
        name: "Admin Logs",
        href: "/admin-logs",
        headerLevel: "H1"
      }
  ];

export const excludedTables = [
    "users",
    "api_keys"
]