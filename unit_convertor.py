import streamlit as st

# Speed unit options
speed_units = ['m/min', 'm/sec', 'mm/min', 'mm/sec']

# Conversion functions
def convert_speed(value, from_unit, to_unit):
    conversion_factors = {
        ('m/min', 'm/sec'): 1/60,
        ('m/min', 'mm/min'): 1000,
        ('m/min', 'mm/sec'): 1000/60,
        ('m/sec', 'm/min'): 60,
        ('m/sec', 'mm/min'): 60000,
        ('m/sec', 'mm/sec'): 1000,
        ('mm/min', 'm/min'): 1/1000,
        ('mm/min', 'm/sec'): 1/60000,
        ('mm/min', 'mm/sec'): 1/60,
        ('mm/sec', 'm/min'): 60/1000,
        ('mm/sec', 'm/sec'): 1/1000,
        ('mm/sec', 'mm/min'): 60,
    }
    conversion_factor = conversion_factors[(from_unit, to_unit)]
    converted_value = value * conversion_factor
    return converted_value

# Streamlit UI
st.title("Line Speed Converter")

from_speed_unit = st.selectbox("Select the initial speed unit:", speed_units)
value = st.number_input("Enter a value:", value=0.00, step=0.1)
to_speed_unit = st.selectbox("Select the target speed unit:", speed_units)

if st.button("Convert"):
    converted_value = convert_speed(value, from_speed_unit, to_speed_unit)
    st.success(f"{value} {from_speed_unit} is equal to {converted_value:.2f} {to_speed_unit}")

