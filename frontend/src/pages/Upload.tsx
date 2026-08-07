import { useState } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

import { pdfService } from "../services/pdfService";

export default function Upload() {
    const navigate = useNavigate();

    const [file, setFile] = useState<File | null>(null);
    const [loading, setLoading] = useState(false);

    async function handleUpload() {
        if (!file) {
            toast.error("Please select a PDF.");
            return;
        }

        try {
            setLoading(true);

            const result = await pdfService.upload(file);

            toast.success("Quiz generated!");

            navigate(`/quiz/${result.quiz_id}`);
        } catch {
            toast.error("Upload failed.");
        } finally {
            setLoading(false);
        }
    }

    return (
        <div className="flex min-h-screen items-center justify-center bg-slate-100">
            <div className="w-full max-w-xl rounded-xl bg-white p-8 shadow-lg">

                <h1 className="mb-6 text-3xl font-bold">
                    Upload PDF
                </h1>

                <input
                    type="file"
                    accept=".pdf"
                    onChange={(e) =>
                        setFile(
                            e.target.files?.[0] ?? null
                        )
                    }
                    className="mb-6 w-full"
                />

                <button
                    onClick={handleUpload}
                    disabled={loading}
                    className="w-full rounded bg-blue-600 p-3 text-white hover:bg-blue-700"
                >
                    {loading
                        ? "Generating Quiz..."
                        : "Generate Quiz"}
                </button>

            </div>
        </div>
    );
}