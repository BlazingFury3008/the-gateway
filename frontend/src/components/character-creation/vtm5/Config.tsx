import React from "react";
import { config_interface } from "@/data/vtm5_characterCreation";
import VTM5Config from "../configuration/vtm5_config";

export default function Config({
  configOption,
  setConfigOptions,
}: {
  configOption: config_interface;
  setConfigOptions: (data: config_interface) => void;
}) {
  return (
    <div>
            <div className="text-center">
        <h2 className="text-lg font-semibold text-[var(--color-foreground)]">Character Configuration</h2>
      </div>
      <VTM5Config configOption={configOption} setConfigOptions={setConfigOptions} />

    </div>
  )
}
