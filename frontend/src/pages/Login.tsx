import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

import { authService } from "../services/authService";
import { useAuth } from "../contexts/AuthContext";

interface LoginForm {
    email: string;
    password: string;
}

export default function Login() {
    const navigate = useNavigate();
    const { login } = useAuth();

    const {
        register,
        handleSubmit,
        formState: { isSubmitting },
    } = useForm<LoginForm>();

    async function onSubmit(data: LoginForm) {
        try {
            const response = await authService.login(data);

            login(response.access_token);

            toast.success("Login successful!");

            navigate("/dashboard");
        } catch {
            toast.error("Invalid email or password");
        }
    }

    return (
        <div className="flex min-h-screen items-center justify-center bg-slate-100">
            <form
                onSubmit={handleSubmit(onSubmit)}
                className="w-full max-w-md rounded-lg bg-white p-8 shadow-lg"
            >
                <h1 className="mb-6 text-center text-3xl font-bold">
                    QuizKarteHai
                </h1>

                <input
                    type="email"
                    placeholder="Email"
                    {...register("email", { required: true })}
                    className="mb-4 w-full rounded border p-3"
                />

                <input
                    type="password"
                    placeholder="Password"
                    {...register("password", { required: true })}
                    className="mb-6 w-full rounded border p-3"
                />

                <button
                    type="submit"
                    disabled={isSubmitting}
                    className="w-full rounded bg-blue-600 p-3 text-white hover:bg-blue-700"
                >
                    {isSubmitting ? "Logging in..." : "Login"}
                </button>
            </form>
        </div>
    );
}