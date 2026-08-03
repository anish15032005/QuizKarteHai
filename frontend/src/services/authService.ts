import { api } from "../api/client";

export interface LoginRequest {
    email: string;
    password: string;
}

export interface LoginResponse {
    access_token: string;
    token_type: string;
}

export interface RegisterRequest {
    name: string;
    email: string;
    password: string;
}

export const authService = {
    async login(data: LoginRequest): Promise<LoginResponse> {
        const response = await api.post("/auth/login", data);
        return response.data;
    },

    async register(data: RegisterRequest) {
        const response = await api.post("/users", data);
        return response.data;
    },

    logout() {
        localStorage.removeItem("token");
    },

    saveToken(token: string) {
        localStorage.setItem("token", token);
    },

    getToken() {
        return localStorage.getItem("token");
    },

    isAuthenticated() {
        return !!localStorage.getItem("token");
    },
};