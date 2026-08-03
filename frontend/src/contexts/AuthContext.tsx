import {
    createContext,
    useContext,
    useState,
} from "react";

interface AuthContextType {
    token: string | null;
    login: (token: string) => void;
    logout: () => void;
    isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({
    children,
}: {
    children: React.ReactNode;
}) {
    const [token, setToken] = useState<string | null>(() =>
        localStorage.getItem("token")
    );

    function login(token: string) {
        localStorage.setItem("token", token);
        setToken(token);
    }

    function logout() {
        localStorage.removeItem("token");
        setToken(null);
    }

    return (
        <AuthContext.Provider
            value={{
                token,
                login,
                logout,
                isAuthenticated: !!token,
            }}
        >
            {children}
        </AuthContext.Provider>
    );
}

// eslint-disable-next-line react-refresh/only-export-components
export function useAuth() {
    const context = useContext(AuthContext);

    if (!context) {
        throw new Error("useAuth must be used inside AuthProvider");
    }

    return context;
}