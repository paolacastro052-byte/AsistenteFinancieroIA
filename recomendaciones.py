def generar_recomendacion(categoria):

    recomendaciones = {

        "Comida":
        "Reduce gastos frecuentes en comida rápida.",

        "Entretenimiento":
        "Mantén equilibrio entre entretenimiento y ahorro.",

        "Transporte":
        "Considera opciones de transporte más económicas.",

        "Salud":
        "Los gastos en salud son importantes para tu bienestar.",

        "Educación":
        "Invertir en educación aporta crecimiento profesional.",

        "Servicios":
        "Controla el consumo mensual de servicios.",

        "Compras":
        "Evita compras impulsivas.",

        "Hogar":
        "Planifica mejor los gastos del hogar."
    }

    return recomendaciones.get(
        categoria,
        "No hay recomendación disponible."
    )