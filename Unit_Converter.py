import streamlit as st
import pint

st.title("Unit Converter")

ureg = pint.UnitRegistry()
ureg.load_definitions('unit_def.txt') # doctest: +SKIP

inputQuantity = None
convertedQuantity = None

#単位
#Length
lengthUnit = {
    "mm":"millimeter",
    "cm":"centimeter",
    "m":"meter",
    "km":"kilometer"
}

length2Unit = {
    "mm^2":"millimeter_2",
    "cm^2":"centimeter_2",
    "m^2":"meter_2",
}

length3Unit = {
    "mm^3":"millimeter_3",
    "cm^3":"centimeter_3",
    "m^3":"meter_3",
}

length4Unit = {
    "mm^4":"millimeter_4",
    "cm^4":"centimeter_4",
    "m^4":"meter_4",
}

massUnit = {
    "g":"gram",
    "kg":"kilogram",
    "t (metric ton)":"metric_ton",
    "US ton (short ton)":"US_ton",
    "UK ton (long ton)":"UK_ton"

}

timeUnit = {
    "sec.":"second",
    "min.":"minute",
    "hour":"hour",
    "Day":"day",
    "Week":"week",
    "Month":"month",
    "Year":"year"
}

#Type
type = {
    "Length, 長さ":lengthUnit,
    "Length^2, 長さの2乗, 面積":length2Unit,
    "Length^3, 長さの3乗, 体積":length3Unit,
    "Length^4, 長さの4乗":length4Unit,
    "Mass, 質量":massUnit,
    "Time, 時間":timeUnit
}


colU1, colU2, colU3 = st.columns([2,1,1])

with colU1:
    inputNum = st.number_input("換算する数値", value=10, step=None)

with colU2:
    inputUnitType = st.selectbox(
        "単位の種別",
        type.keys(),
        key="type"
    )

with colU3:
    inputUnit = st.selectbox(
        "単位",
        type[inputUnitType].keys(),
        key="input"
    )

inputQuantity = ureg.Quantity(inputNum, type[inputUnitType][inputUnit])

convertedQuantity = inputQuantity
#st.write(unit[inputUnit])

st.markdown("<h2 style='text-align: center;'>↓</h2>", unsafe_allow_html=True)

colL1, colL2 = st.columns([3,1])
with colL2:
    convertedUnit = st.selectbox(
        "単位",
        type[inputUnitType].keys(),
        key="output"
    )

convertedQuantity = inputQuantity.to(type[inputUnitType][convertedUnit])

with colL1:
    st.markdown(f"<p style='text-align: center; font-size: 35px; height:100px; line-height:100px;'>{convertedQuantity.magnitude}</p>", unsafe_allow_html=True)


#st.write(list(ureg))




