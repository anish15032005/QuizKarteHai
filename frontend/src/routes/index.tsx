import { createBrowserRouter } from "react-router-dom";

import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Upload from "../pages/Upload";
import Quiz from "../pages/Quiz";
import Result from "../pages/Result";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <Login />,
    },
    {
        path: "/dashboard",
        element: <Dashboard />,
    },
    {
        path: "/upload",
        element: <Upload />,
    },
    {
        path: "/quiz/:id",
        element: <Quiz />,
    },
    {
        path: "/result/:id",
        element: <Result />,
    },
]);