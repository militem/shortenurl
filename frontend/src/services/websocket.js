export default class WebSocketService {
    constructor(url) {
        this.url = url;
        this.socket = null;
    }

    connect(onMessage, onError) {
        this.socket = new WebSocket(this.url);

        this.socket.onopen = () => {
            console.log("WebSocket conectado:", this.url);
        };

        this.socket.onmessage = (event) => {
            console.log("Mensaje recibido:", event.data);
            if (onMessage) onMessage(event.data);
        };

        this.socket.onerror = (error) => {
            console.error("Error en WebSocket:", error);
            if (onError) onError(error);
        };

        this.socket.onclose = () => {
            console.log("WebSocket cerrado.");
        };
    }

    sendMessage(message) {
        if (this.socket && this.socket.readyState === WebSocket.OPEN) {
            this.socket.send(message);
        } else {
            console.error("No se puede enviar el mensaje, WebSocket no está conectado.");
        }
    }

    close() {
        if (this.socket) {
            this.socket.close();
        }
    }
}