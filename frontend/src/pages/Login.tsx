import { authService } from "../services/authService";

export default function Login() {
    async function testLogin() {
        try {
            const response = await authService.login({
                email: "anish@example.com",
                password: "12345678",
            });

            console.log(response);
        } catch (error) {
            console.error(error);
        }
    }

    return (
        <div className="flex min-h-screen items-center justify-center">
            <button
                onClick={testLogin}
                className="rounded bg-blue-600 px-6 py-3 text-white"
            >
                Test Login
            </button>
        </div>
    );
}