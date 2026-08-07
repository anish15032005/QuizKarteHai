import { useNavigate } from "react-router-dom";

import { useAuth } from "../contexts/AuthContext";

export default function Dashboard() {
    const navigate = useNavigate();
    const { logout } = useAuth();

    function handleLogout() {
        logout();
        navigate("/");
    }

    return (
        <div className="min-h-screen bg-slate-100">
            <div className="mx-auto max-w-5xl p-8">
                <h1 className="mb-2 text-4xl font-bold">
                    QuizKarteHai
                </h1>

                <p className="mb-10 text-slate-600">
                    Welcome back 👋
                </p>

                <div className="grid gap-6 md:grid-cols-2">

                    <div
                        onClick={() => navigate("/upload")}
                        className="cursor-pointer rounded-xl bg-blue-600 p-8 text-white shadow transition hover:scale-105"
                    >
                        <h2 className="mb-2 text-2xl font-bold">
                            📄 Generate Quiz
                        </h2>

                        <p>
                            Upload a PDF and let AI generate a quiz.
                        </p>
                    </div>

                    <div
                        onClick={() => navigate("/quizzes")}    
                        className="cursor-pointer rounded-xl bg-white p-8 shadow transition hover:scale-105"
                    >
                        <h2 className="mb-2 text-2xl font-bold">
                            📚 Previous Quizzes
                        </h2>

                        <p>
                            View quizzes you've already generated.
                        </p>
                    </div>

                </div>

                <button
                    onClick={handleLogout}
                    className="mt-12 rounded bg-red-600 px-6 py-3 text-white hover:bg-red-700"
                >
                    Logout
                </button>
            </div>
        </div>
    );
}