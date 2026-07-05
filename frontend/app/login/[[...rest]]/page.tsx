import { SignIn } from "@clerk/nextjs";

export default function LoginPage() {
  return (
    <div className="flex flex-1 items-center justify-center py-16">
      <SignIn path="/login" routing="path" signUpUrl="/signup" fallbackRedirectUrl="/onboarding" />
    </div>
  );
}
