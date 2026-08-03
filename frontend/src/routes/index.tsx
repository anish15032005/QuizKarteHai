// frontend/src/routes/index.tsx

import { createBrowserRouter } from "react-router-dom";

import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Upload from "../pages/Upload";
import Quiz from "../pages/Quiz";
import Result from "../pages/Result";

import ProtectedRoute from "../components/ProtectedRoute";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <Login />,
    },
    {
        path: "/dashboard",
        element: (
            <ProtectedRoute>
                <Dashboard />
            </ProtectedRoute>
        ),
    },
    {
        path: "/upload",
        element: (
            <ProtectedRoute>
                <Upload />
            </ProtectedRoute>
        ),
    },
    {
        path: "/quiz/:id",
        element: (
            <ProtectedRoute>
                <Quiz />
            </ProtectedRoute>
        ),
    },
    {
        path: "/result/:id",
        element: (
            <ProtectedRoute>
                <Result />
            </ProtectedRoute>
        ),
    },
]);