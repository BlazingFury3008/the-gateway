import { config_interface } from '@/data/vtm5_characterCreation';
import { Check, X } from 'lucide-react';
import React from 'react';

export default function VTM5Config({
  configOption,
  setConfigOptions,
  editable = true,
}: {
  configOption: config_interface;
  setConfigOptions: (data: config_interface) => void;
  editable?: boolean;
}) {
  const handleChange = (key: keyof config_interface, value: string | boolean | number) => {
    setConfigOptions({ ...configOption, [key]: value });
  };

  const checkboxes = [
    { key: "variantBane", label: "Enable Variant Bane" },
    { key: "additionalFlaw", label: "Allow Additional Flaws" },
    { key: "ritualPerLevel", label: "Rituals Per Level" },
    { key: "no_cap", label: "Remove Power Cap" },
    { key: "noprereq", label: "Ignore Prerequisites" },
    { key: "loresheets", label: "Enable Loresheets" },
  ];

  const experienceOptions = [
    { key: "none", label: "No Experience" },
    { key: "touch-up", label: "Touch Up (+10xp)" },
    { key: "established", label: "Established Kindred (+30xp)" },
    { key: "major", label: "Major Player (+50xp)" },
    { key: "legend", label: "Local Legend (+70xp)" },
    { key: "number", label: "Custom Experience" },
  ];

  return (
    <section className="px-4 sm:px-8 py-10 max-w-screen-xl mx-auto space-y-12">
      {/* Section: Feature Toggles */}
      <div className="bg-[var(--color-form)] p-6 rounded-2xl shadow-md border border-[var(--color-border)]">
        <h3 className="text-lg font-semibold text-[var(--color-foreground)] mb-4">Game Features</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-4">
          {checkboxes.map(({ key, label }) => (
            <ToggleCard
              key={key}
              label={label}
              value={configOption[key as keyof config_interface] as boolean}
              onChange={(val) => handleChange(key as keyof config_interface, val)}
              disabled={!editable}
            />
          ))}
        </div>
      </div>

      {/* Section: XP Dropdown */}
      <div className="bg-[var(--color-form)] p-6 rounded-2xl shadow-md border border-[var(--color-border)] mx-auto">
        <h3 className="text-lg font-semibold text-[var(--color-foreground)] mb-4">Experience Setup</h3>
        <div className="flex flex-col gap-4">
          <div className="space-y-1">
            <label htmlFor="experience" className="text-sm font-medium text-[var(--color-foreground)]">
              Starting Experience
            </label>
            <select
              id="experience"
              name="experience"
              disabled={!editable}
              value={configOption.additionalXP}
              onChange={(e) => handleChange("additionalXP", e.target.value)}
              className="input bg-[var(--color-background)] appearance-none focus:ring-2 focus:ring-[var(--color-primary)]"
            >
              {experienceOptions.map(({ key, label }) => (
                <option key={key} value={key}>
                  {label}
                </option>
              ))}
            </select>
          </div>

          {configOption.additionalXP === "number" && (
            <div className="space-y-1">
              <label htmlFor="customXP" className="text-sm font-medium text-[var(--color-foreground)]">
                Custom XP Amount
              </label>
              <input
                id="customXP"
                type="number"
                min={0}
                value={configOption.customXP ?? 0}
                onChange={(e) => handleChange("customXP", parseInt(e.target.value, 10))}
                disabled={!editable}
                className="input bg-[var(--color-background)]"
                placeholder="Enter XP amount"
              />
            </div>
          )}
        </div>
      </div>
    </section>
  );
}

function ToggleCard({
  label,
  value,
  onChange,
  disabled,
}: {
  label: string;
  value: boolean;
  onChange: (val: boolean) => void;
  disabled?: boolean;
}) {
  return (
    <button
      onClick={() => !disabled && onChange(!value)}
      disabled={disabled}
      className={`w-full flex items-center justify-between p-4 rounded-xl border transition-all shadow-sm
        ${
          disabled
            ? "opacity-50 cursor-not-allowed"
            : "hover:shadow-md hover:bg-[var(--color-background-hover)] cursor-pointer"
        }
        bg-[var(--color-background)] border-[var(--color-border)]`}
    >
      <span className="text-sm font-medium text-[var(--color-foreground)]">{label}</span>
      <span className={`${value ? "text-[var(--color-success)]" : "text-[var(--color-danger)]"}`}>
        {value ? <Check size={20} /> : <X size={20} />}
      </span>
    </button>
  );
}
