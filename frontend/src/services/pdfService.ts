import { api } from "../api/client";

export const pdfService = {
    async upload(file: File) {
        const formData = new FormData();

        formData.append("file", file);

        const response = await api.post(
            "/pdf/upload",
            formData,
            {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            }
        );

        return response.data;
    },
};