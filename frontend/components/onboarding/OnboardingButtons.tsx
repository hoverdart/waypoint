import { ComponentProps } from "react";
import { Button } from "@/components/ui/button";
import { WayPointButton } from "@/components/shared/WayPointButton";

type ButtonPropsWithoutVariant = Omit<ComponentProps<typeof Button>, "variant">;

export function PrimaryButton(props: ButtonPropsWithoutVariant) {
  return <WayPointButton variant="primary" {...props} />;
}

export function SecondaryButton(props: ButtonPropsWithoutVariant) {
  return <WayPointButton variant="ghost" {...props} />;
}
