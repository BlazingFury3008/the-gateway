import { useState } from "react";

type SearchableDropdownProps<T> = {
  items: T[];
  value: T | null;
  onChange: (value: T | null) => void;
  getLabel: (item: T) => string;
  getKey: (item: T) => string | number;
  placeholder?: string;
};

export function SearchableDropdown<T>({
  items,
  value,
  onChange,
  getLabel,
  getKey,
  placeholder = "-- Select --",
}: SearchableDropdownProps<T>) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");

  const filtered = items.filter((item) =>
    getLabel(item).toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div className="sd-root">
      <input
        type="text"
        placeholder={placeholder}
        value={open ? query : value ? getLabel(value) : ""}
        onFocus={() => setOpen(true)}
        onBlur={() => setOpen(false)}
        onChange={(e) => {
          setQuery(e.target.value);
          setOpen(true);
        }}
        className="sd-input"
      />

      {open && (
        <div className="sd-menu">
          <button
            type="button"
            className="sd-item sd-item-muted"
            // use onMouseDown so click registers before blur closes the menu
            onMouseDown={(e) => {
              e.preventDefault();
              onChange(null);
              setQuery("");
              setOpen(false);
            }}
          >
            -- None --
          </button>

          {filtered.map((item) => (
            <button
              type="button"
              key={getKey(item)}
              className="sd-item"
              onMouseDown={(e) => {
                e.preventDefault();
                onChange(item);
                setQuery("");
                setOpen(false);
              }}
            >
              {getLabel(item)}
            </button>
          ))}

          {filtered.length === 0 && (
            <div className="sd-empty">No results</div>
          )}
        </div>
      )}
    </div>
  );
}
