import { LoginScreen } from "@/components/auth/LoginScreen";

function safeReturnTo(value: string | undefined): string {
  return value && value.startsWith("/") && !value.startsWith("//") && !value.startsWith("/\\") ? value : "/dashboard";
}

export default async function LoginPage({ searchParams }: { searchParams: Promise<{ redirect_url?: string }> }) {
  const { redirect_url: redirectUrl } = await searchParams;
  return <LoginScreen returnTo={safeReturnTo(redirectUrl)} />;
}
