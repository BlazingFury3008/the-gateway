import { optionalRulesSelection } from "./vtm5_characterCreation";

export interface ConfigOption {
    header: string;
    id: string; // Unique identifier for each section
    header_level: "H1" | "H2" | "H3" | "label";
    options: {
      [key: string]: {
        type: "boolean" | "number" | "string" | "enum";
        default: boolean | number | string;
        options?: string[]; // Used for enums
      };
    };
  }
  
  

  export const user_configuration: ConfigOption[] = [
    {
      header: "VTM V5",
      id: "vtm_v5",
      header_level: "H1",
      options: Object.fromEntries(
        optionalRulesSelection.map((rule) => [
          rule.label,
          { label: rule.label, type: "boolean", default: false } as const,
        ])
      ),
    },
  ];
  
  

  export interface SavedConfigOption {
    id: string; // Unique identifier for each section
    options: {
      [key: string]: {
        type: "boolean" | "number" | "string" | "enum" | "nested";
        default: boolean | number | string;
        options?: string[]; // Used for enums
      };
    };
  }
  
  export function convertConfigToSaved(config: ConfigOption[]) : SavedConfigOption[] {
    return config.map((category) => {
        return {
            id: category.id,
            options: category.options
          };
    });

  }
  