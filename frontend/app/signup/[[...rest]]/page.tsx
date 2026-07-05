import { SignUp } from "@clerk/nextjs";

export default function SignupPage() {
  return (
    <div className="flex flex-1 items-center justify-center py-16">
      <SignUp path="/signup" routing="path" signInUrl="/login" fallbackRedirectUrl="/onboarding" />
    </div>
  );
}
