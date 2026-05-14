import streamlit as st
import re

# ======================================
# CONFIGURACIÓN
# ======================================

st.set_page_config(
    page_title="Asistente Financiero Inteligente",
    page_icon="💰",
    layout="centered"
)

# ======================================
# FORMATO MONEDA
# ======================================

def campo_moneda(label, key):

    def actualizar():

        valor = st.session_state[key]

        numeros = re.sub(r'[^0-9]', '', valor)

        if numeros != "":

            numero = int(numeros)

            st.session_state[key] = (
                f"${numero:,}".replace(",", ".")
            )

        else:

            st.session_state[key] = ""

    if key not in st.session_state:
        st.session_state[key] = ""

    return st.text_input(
        label,
        key=key,
        on_change=actualizar
    )

# ======================================
# LIMPIAR MONEDA
# ======================================

def limpiar_moneda(valor):

    valor = str(valor)

    valor = valor.replace("$", "")
    valor = valor.replace(".", "")

    if valor == "":
        return 0

    return int(valor)

# ======================================
# TÍTULO
# ======================================

st.title("Asistente Financiero Inteligente")

st.write(
    "Aplicación de Inteligencia Artificial para analizar ingresos, gastos, ahorro y nivel financiero."
)

st.markdown("---")

# ======================================
# COLUMNAS
# ======================================

col1, espacio, col2 = st.columns([1, 0.08, 1])

# ======================================
# INGRESOS
# ======================================

with col1:

    with st.container(border=True):

        st.subheader("Ingresos")

        salario = campo_moneda(
            "Salario mensual",
            "salario"
        )

        otros_ingresos = campo_moneda(
            "Otros ingresos",
            "otros_ingresos"
        )

        st.markdown("---")

        st.subheader("Familia y educación")

        hijos = st.number_input(
            "Cantidad de hijos",
            min_value=0,
            step=1
        )

        colegio = campo_moneda(
            "Pago de colegio",
            "colegio"
        )

        universidad = campo_moneda(
            "Pago de universidad",
            "universidad"
        )

# ======================================
# GASTOS
# ======================================

with col2:

    with st.container(border=True):

        st.subheader("Gastos mensuales")

        alimentacion = campo_moneda(
            "Alimentación",
            "alimentacion"
        )

        transporte = campo_moneda(
            "Transporte",
            "transporte"
        )

        vestimenta = campo_moneda(
            "Vestimenta",
            "vestimenta"
        )

        entretenimiento = campo_moneda(
            "Entretenimiento",
            "entretenimiento"
        )

        arriendo = campo_moneda(
            "Arriendo o hipoteca",
            "arriendo"
        )

        servicios = campo_moneda(
            "Servicios públicos",
            "servicios"
        )

        st.markdown("---")

        st.subheader("Deudas")

        credito = campo_moneda(
            "Pago tarjeta de crédito",
            "credito"
        )

        otras_deudas = campo_moneda(
            "Otras deudas",
            "otras_deudas"
        )

        interes_credito = st.number_input(
            "Interés tarjeta de crédito (%)",
            min_value=0.0,
            max_value=100.0,
            step=0.1
        )

        interes_hipoteca = st.number_input(
            "Interés hipoteca o préstamo (%)",
            min_value=0.0,
            max_value=100.0,
            step=0.1
        )

# ======================================
# PARTE INFERIOR
# ======================================

st.markdown("")

col3, espacio2, col4 = st.columns([1, 0.08, 1])

with col3:

    with st.container(border=True):

        st.subheader("Compras no esenciales")

        compras = campo_moneda(
            "Compras innecesarias",
            "compras"
        )

with col4:

    with st.container(border=True):

        st.subheader("Meta de ahorro anual")

        meta = campo_moneda(
            "¿Cuánto deseas ahorrar en un año?",
            "meta"
        )

st.markdown("")

# ======================================
# BOTÓN
# ======================================

if st.button("Analizar situación financiera"):

    # ======================================
    # LIMPIAR DATOS
    # ======================================

    salario_num = limpiar_moneda(salario)
    otros_ingresos_num = limpiar_moneda(otros_ingresos)

    alimentacion_num = limpiar_moneda(alimentacion)
    transporte_num = limpiar_moneda(transporte)
    vestimenta_num = limpiar_moneda(vestimenta)
    entretenimiento_num = limpiar_moneda(entretenimiento)
    arriendo_num = limpiar_moneda(arriendo)
    servicios_num = limpiar_moneda(servicios)

    colegio_num = limpiar_moneda(colegio)
    universidad_num = limpiar_moneda(universidad)

    credito_num = limpiar_moneda(credito)
    otras_deudas_num = limpiar_moneda(otras_deudas)

    compras_num = limpiar_moneda(compras)

    meta_num = limpiar_moneda(meta)

    # ======================================
    # INGRESOS Y GASTOS
    # ======================================

    ingresos_totales = salario_num + otros_ingresos_num

    gastos_totales = (
        alimentacion_num +
        transporte_num +
        vestimenta_num +
        entretenimiento_num +
        arriendo_num +
        servicios_num +
        colegio_num +
        universidad_num +
        credito_num +
        otras_deudas_num +
        compras_num
    )

    saldo = ingresos_totales - gastos_totales

    # ======================================
    # PORCENTAJE
    # ======================================

    if ingresos_totales > 0:

        porcentaje_gasto = (
            gastos_totales / ingresos_totales
        ) * 100

    else:

        porcentaje_gasto = 0

    # ======================================
    # SCORE
    # ======================================

    if porcentaje_gasto <= 50:

        score = 90

    elif porcentaje_gasto <= 70:

        score = 70

    elif porcentaje_gasto <= 90:

        score = 50

    else:

        score = 30

    # ======================================
    # DASHBOARD
    # ======================================

    st.markdown("---")

    st.header("Dashboard financiero")

    d1, d2, d3 = st.columns(3)

    with d1:

        with st.container(border=True):

            st.metric(
                "Ingresos",
                f"${ingresos_totales:,.0f}".replace(",", ".")
            )

    with d2:

        with st.container(border=True):

            st.metric(
                "Gastos",
                f"${gastos_totales:,.0f}".replace(",", ".")
            )

    with d3:

        with st.container(border=True):

            st.metric(
                "Disponible",
                f"${saldo:,.0f}".replace(",", ".")
            )

    st.markdown("")

    d4, d5 = st.columns(2)

    with d4:

        with st.container(border=True):

            st.metric(
                "% Gastos",
                f"{porcentaje_gasto:.1f}%"
            )

    with d5:

        with st.container(border=True):

            st.metric(
                "Score financiero",
                f"{score}/100"
            )

    # ======================================
    # ANÁLISIS IA
    # ======================================

    st.markdown("---")

    st.header("Análisis inteligente")

    if porcentaje_gasto >= 90:

        st.error(
            "Tu nivel de gasto es muy alto y representa un riesgo financiero."
        )

    elif porcentaje_gasto >= 70:

        st.warning(
            "Tus gastos son elevados. Se recomienda reducir gastos no esenciales."
        )

    else:

        st.success(
            "Tu nivel de gasto es saludable."
        )

    # ======================================
    # RECOMENDACIONES
    # ======================================

    st.header("Recomendaciones financieras")

    if compras_num > 0:

        st.write(
            "- Reduce las compras innecesarias para mejorar tu capacidad de ahorro."
        )

    if entretenimiento_num > 300000:

        st.write(
            "- Tus gastos en entretenimiento son elevados."
        )

    if credito_num > 0:

        st.write(
            "- Prioriza el pago de tarjetas de crédito para reducir intereses."
        )

    # ======================================
    # PLAN DE DEUDA
    # ======================================

    st.header("Plan de reducción de deuda")

    deuda_total = credito_num + otras_deudas_num

    if deuda_total > 0:

        pago_sugerido = saldo * 0.30

        deuda1, deuda2 = st.columns(2)

        with deuda1:

            with st.container(border=True):

                st.metric(
                    "Deuda total",
                    f"${deuda_total:,.0f}".replace(",", ".")
                )

        with deuda2:

            with st.container(border=True):

                st.metric(
                    "Pago sugerido mensual",
                    f"${pago_sugerido:,.0f}".replace(",", ".")
                )

                st.caption(
                    "La IA recomienda destinar el 30% del dinero disponible al pago de deuda."
                )

        st.info(
            "Este plan busca reducir intereses sin afectar tu estabilidad financiera."
        )

    else:

        st.success(
            "Actualmente no registras deudas importantes."
        )

    # ======================================
    # ESTRATEGIAS IA
    # ======================================

    st.markdown("---")

    st.header("Estrategias inteligentes IA")

    # ======================================
    # INTERESES
    # ======================================

    st.subheader("Análisis de intereses")

    if interes_credito >= 5:

        st.error(
            "La tarjeta de crédito tiene un interés elevado."
        )

        st.write(
            "- La IA recomienda priorizar esta deuda."
        )

    elif interes_credito > 0:

        st.warning(
            "La tarjeta tiene un interés moderado."
        )

    if interes_hipoteca >= 3:

        st.warning(
            "Tu préstamo hipotecario tiene un interés considerable."
        )

        st.write(
            "- Evalúa pagos adicionales para reducir intereses futuros."
        )

    # ======================================
    # AHORRO IA
    # ======================================

    st.subheader("Plan inteligente de ahorro")

    if saldo > 0:

        ahorro_ideal = ingresos_totales * 0.20

        ahorro_semanal = ahorro_ideal / 4

        ahorro_anual = ahorro_ideal * 12

        st.write(
            "La IA recomienda ahorrar el 20% de tus ingresos."
        )

        st.markdown("")

        a1, a2, a3 = st.columns(3)

        with a1:

            st.metric(
                "Ahorro semanal",
                f"${ahorro_semanal:,.0f}".replace(",", ".")
            )

            st.caption(
                "Proyección semanal recomendada"
            )

        with a2:

            st.metric(
                "Ahorro mensual",
                f"${ahorro_ideal:,.0f}".replace(",", ".")
            )

            st.caption(
                "Meta mensual sugerida"
            )

        with a3:

            st.metric(
                "Proyección anual",
                f"${ahorro_anual:,.0f}".replace(",", ".")
            )

            st.caption(
                "Ahorro estimado en un año"
            )

        st.markdown("")

        # ======================================
        # VALIDACIÓN META ANUAL
        # ======================================

        if ahorro_anual >= meta_num:

            st.success(
                "Tu capacidad financiera actual sí permite alcanzar esta meta anual."
            )

            ok1, ok2, ok3 = st.columns(3)

            with ok1:

                st.metric(
                    "Meta anual",
                    f"${meta_num:,.0f}".replace(",", ".")
                )

            with ok2:

                st.metric(
                    "Capacidad anual",
                    f"${ahorro_anual:,.0f}".replace(",", ".")
                )

            with ok3:

                diferencia = ahorro_anual - meta_num

                st.metric(
                    "Margen adicional",
                    f"${diferencia:,.0f}".replace(",", ".")
                )

            st.info(
                "Manteniendo disciplina financiera podrías cumplir tu objetivo anual de ahorro."
            )

        else:

            faltante = meta_num - ahorro_anual

            ahorro_semanal_meta = meta_num / 52

            ahorro_mensual_meta = meta_num / 12

            st.warning(
                "Tu capacidad actual no alcanza la meta anual deseada."
            )

            meta1, meta2, meta3 = st.columns(3)

            with meta1:

                st.metric(
                    "Ahorro semanal requerido",
                    f"${ahorro_semanal_meta:,.0f}".replace(",", ".")
                )

            with meta2:

                st.metric(
                    "Ahorro mensual requerido",
                    f"${ahorro_mensual_meta:,.0f}".replace(",", ".")
                )

            with meta3:

                st.metric(
                    "Meta anual",
                    f"${meta_num:,.0f}".replace(",", ".")
                )

            st.info(
                f"Actualmente podrías ahorrar aproximadamente ${ahorro_anual:,.0f} al año.".replace(",", ".")
            )

            st.write(
                f"- Necesitas aumentar aproximadamente ${faltante:,.0f} anuales.".replace(",", ".")
            )

            st.write(
                "- Reduce gastos variables y compras innecesarias."
            )

            st.write(
                "- Considera ingresos adicionales o ahorro automático."
            )

    else:

        st.error(
            "Actualmente tus gastos superan tus ingresos."
        )

        st.write(
            "- Activa modo ahorro extremo."
        )

        st.write(
            "- Reduce entretenimiento y compras innecesarias."
        )

        st.write(
            "- Prioriza pagos esenciales."
        )

    # ======================================
    # MÉTODOS IA
    # ======================================

    st.markdown("---")

    t1, t2 = st.columns(2)

    with t1:

        with st.container(border=True):

            st.subheader("Método bola de nieve")

            st.write(
                "• Paga primero las deudas más pequeñas."
            )

            st.write(
                "• Cada deuda eliminada libera más dinero mensual."
            )

            st.write(
                "• Mejora motivación y control financiero."
            )

    with t2:

        with st.container(border=True):

            st.subheader("Método avalancha")

            st.write(
                "• Prioriza las deudas con intereses más altos."
            )

            st.write(
                "• Reduce el pago total de intereses."
            )

            st.write(
                "• Método matemáticamente más eficiente."
            )

    st.markdown("")

    t3, t4 = st.columns(2)

    with t3:

        with st.container(border=True):

            st.subheader("Nivel financiero")

            if porcentaje_gasto <= 50:

                st.success(
                    "Nivel financiero saludable."
                )

            elif porcentaje_gasto <= 70:

                st.warning(
                    "Nivel financiero intermedio."
                )

            else:

                st.error(
                    "Nivel financiero de riesgo."
                )

    with t4:

        with st.container(border=True):

            st.subheader("Capacidad financiera anual IA")

            if saldo > 0:

                proyeccion = saldo * 12

                st.metric(
                    "Capacidad de ahorro anual",
                    f"${proyeccion:,.0f}".replace(",", ".")
                )

            else:

                st.error(
                    "Posible aumento de deuda."
                )