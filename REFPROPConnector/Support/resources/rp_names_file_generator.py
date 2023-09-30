import os

FILE_VERSION="0.3.5"
__CURR_DIR = os.path.dirname(__file__)
__RP_NAMES_TXT = """<?xml version="1.0" encoding="UTF-8" ?>
<data>
    <info version="{fileversion}"/>
    <names>

        <refprop_name name = "P">

            <std_names>

                <std_name name="Pressure"/>
                <std_name name="Pres"/>
                <std_name name="Press"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = "kPa" />
                <unit name = "MOLE SI"          unit = "MPa" />
                <unit name = "MASS SI"          unit = "MPa" />
                <unit name = "SI WITH C"        unit = "MPa" />

                <unit name = "MOLAR BASE SI"    unit = "Pa"  />
                <unit name = "MASS BASE SI"     unit = "Pa"  />
                <unit name = "ENGLISH"          unit = "psia"/>
                <unit name = "MOLAR ENGLISH"    unit = "psia"/>

                <unit name = "MKS"              unit = "kPa" />
                <unit name = "CGS"              unit = "MPa" />
                <unit name = "MIXED"            unit = "psia"/>
                <unit name = "MEUNITS"          unit = "bar" />

            </units>

        </refprop_name>
        <refprop_name name = "T">

            <std_names>

                <std_name name="Temperature"/>
                <std_name name="Temp"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = "K" />
                <unit name = "MOLE SI"          unit = "K" />
                <unit name = "MASS SI"          unit = "K" />
                <unit name = "SI WITH C"        unit = "C" />

                <unit name = "MOLAR BASE SI"    unit = "K" />
                <unit name = "MASS BASE SI"     unit = "K" />
                <unit name = "ENGLISH"          unit = "F" />
                <unit name = "MOLAR ENGLISH"    unit = "F" />

                <unit name = "MKS"              unit = "K" />
                <unit name = "CGS"              unit = "K" />
                <unit name = "MIXED"            unit = "K" />
                <unit name = "MEUNITS"          unit = "C" />

            </units>

        </refprop_name>
        <refprop_name name = "D">

            <std_names>

                <std_name name="rho"/>
                <std_name name="density"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = "mol/dm^3" />
                <unit name = "MOLE SI"          unit = "mol/dm^3" />
                <unit name = "MASS SI"          unit = "kg/m^3" />
                <unit name = "SI WITH C"        unit = "kg/m^3" />

                <unit name = "MOLAR BASE SI"    unit = "mol/m^3" />
                <unit name = "MASS BASE SI"     unit = "kg/m^3" />
                <unit name = "ENGLISH"          unit = "lbm/ft^3" />
                <unit name = "MOLAR ENGLISH"    unit = "lbmol/ft^3" />

                <unit name = "MKS"              unit = "kg/m^3" />
                <unit name = "CGS"              unit = "g/cm^3" />
                <unit name = "MIXED"            unit = "g/cm^3" />
                <unit name = "MEUNITS"          unit = "g/cm^3" />

            </units>

        </refprop_name>
        <refprop_name name = "E">

            <std_names>

                <std_name name="u"/>
                <std_name name="internal_energy"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = "J/mol" />
                <unit name = "MOLE SI"          unit = "J/mol" />
                <unit name = "MASS SI"          unit = "J/g" />
                <unit name = "SI WITH C"        unit = "J/g" />

                <unit name = "MOLAR BASE SI"    unit = "J/mol" />
                <unit name = "MASS BASE SI"     unit = "J/kg" />
                <unit name = "ENGLISH"          unit = "BTU/lbm" />
                <unit name = "MOLAR ENGLISH"    unit = "BTU/lbmol" />

                <unit name = "MKS"              unit = "J/g" />
                <unit name = "CGS"              unit = "J/g" />
                <unit name = "MIXED"            unit = "J/g" />
                <unit name = "MEUNITS"          unit = "J/g" />

            </units>

        </refprop_name>
        <refprop_name name = "H">

            <std_names>

                <std_name name="enthalpy"/>
                <std_name name="enth"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = "J/mol" />
                <unit name = "MOLE SI"          unit = "J/mol" />
                <unit name = "MASS SI"          unit = "J/g" />
                <unit name = "SI WITH C"        unit = "J/g" />

                <unit name = "MOLAR BASE SI"    unit = "J/mol" />
                <unit name = "MASS BASE SI"     unit = "J/kg" />
                <unit name = "ENGLISH"          unit = "BTU/lbm" />
                <unit name = "MOLAR ENGLISH"    unit = "BTU/lbmol" />

                <unit name = "MKS"              unit = "J/g" />
                <unit name = "CGS"              unit = "J/g" />
                <unit name = "MIXED"            unit = "J/g" />
                <unit name = "MEUNITS"          unit = "J/g" />

            </units>

        </refprop_name>
        <refprop_name name = "S">

            <std_names>

                <std_name name="entropy"/>
                <std_name name="entr"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = "J/(mol * K)" />
                <unit name = "MOLE SI"          unit = "J/(mol * K)" />
                <unit name = "MASS SI"          unit = "J/(g * K)" />
                <unit name = "SI WITH C"        unit = "J/(g * K)" />

                <unit name = "MOLAR BASE SI"    unit = "J/(mol * K)" />
                <unit name = "MASS BASE SI"     unit = "J/(kg * K)" />
                <unit name = "ENGLISH"          unit = "BTU/(lbm * R)" />
                <unit name = "MOLAR ENGLISH"    unit = "BTU/(lbmol * R)" />

                <unit name = "MKS"              unit = "J/(g * K)" />
                <unit name = "CGS"              unit = "J/(g * K)" />
                <unit name = "MIXED"            unit = "J/(g * K)" />
                <unit name = "MEUNITS"          unit = "J/(g * K)" />

            </units>

        </refprop_name>
        <refprop_name name = "Q">

            <std_names>

                <std_name name="quality"/>
                <std_name name="x"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = " - " />
                <unit name = "MOLE SI"          unit = " - " />
                <unit name = "MASS SI"          unit = " - " />
                <unit name = "SI WITH C"        unit = " - " />

                <unit name = "MOLAR BASE SI"    unit = " - " />
                <unit name = "MASS BASE SI"     unit = " - " />
                <unit name = "ENGLISH"          unit = " - " />
                <unit name = "MOLAR ENGLISH"    unit = " - " />

                <unit name = "MKS"              unit = " - " />
                <unit name = "CGS"              unit = " - " />
                <unit name = "MIXED"            unit = " - " />
                <unit name = "MEUNITS"          unit = " - " />

            </units>

        </refprop_name>
        <refprop_name name = "VIS">

            <std_names>

                <std_name name="mu"/>
                <std_name name="viscosity"/>
                <std_name name="visc"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = "uPa * s" />
                <unit name = "MOLE SI"          unit = "uPa * s" />
                <unit name = "MASS SI"          unit = "uPa * s" />
                <unit name = "SI WITH C"        unit = "uPa * s" />

                <unit name = "MOLAR BASE SI"    unit = "Pa * s" />
                <unit name = "MASS BASE SI"     unit = "Pa * s" />
                <unit name = "ENGLISH"          unit = "lbm/(ft * s)" />
                <unit name = "MOLAR ENGLISH"    unit = "lbm/(ft * s)" />

                <unit name = "MKS"              unit = "uPa * s" />
                <unit name = "CGS"              unit = "uPa * s" />
                <unit name = "MIXED"            unit = "uPa * s" />
                <unit name = "MEUNITS"          unit = "cpoise" />

            </units>

        </refprop_name>
        <refprop_name name = "TCX">

            <std_names>

                <std_name name="thermal_conductivity"/>
                <std_name name="k"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = "W/(m * K)" />
                <unit name = "MOLE SI"          unit = "mW/(m * K)" />
                <unit name = "MASS SI"          unit = "mW/(m * K)" />
                <unit name = "SI WITH C"        unit = "mW/(m * K)" />

                <unit name = "MOLAR BASE SI"    unit = "W/(m * K)" />
                <unit name = "MASS BASE SI"     unit = "W/(m * K)" />
                <unit name = "ENGLISH"          unit = "BTU/(h * ft * R)" />
                <unit name = "MOLAR ENGLISH"    unit = "BTU/(h * ft * R)" />

                <unit name = "MKS"              unit = "W/(m * K)" />
                <unit name = "CGS"              unit = "mW/(m * K)" />
                <unit name = "MIXED"            unit = "mW/(m * K)" />
                <unit name = "MEUNITS"          unit = "mW/(m * K)" />

            </units>

        </refprop_name>
        <refprop_name name = "CP">

            <std_names>

                <std_name name="cp"/>
                <std_name name="isochoric_heat_capacity"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = "J/(mol * K)" />
                <unit name = "MOLE SI"          unit = "J/(mol * K)" />
                <unit name = "MASS SI"          unit = "J/(g * K)" />
                <unit name = "SI WITH C"        unit = "J/(g * K)" />

                <unit name = "MOLAR BASE SI"    unit = "J/(mol * K)" />
                <unit name = "MASS BASE SI"     unit = "J/(kg * K)" />
                <unit name = "ENGLISH"          unit = "BTU/(lbm * R)" />
                <unit name = "MOLAR ENGLISH"    unit = "BTU/(lbmol * R)" />

                <unit name = "MKS"              unit = "J/(g * K)" />
                <unit name = "CGS"              unit = "J/(g * K)" />
                <unit name = "MIXED"            unit = "J/(g * K)" />
                <unit name = "MEUNITS"          unit = "J/(g * K)" />

            </units>

        </refprop_name>
        <refprop_name name = "CP0">

            <std_names>

                <std_name name="cp0"/>
                <std_name name="ideal_isochoric_heat_capacity"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = "J/(mol * K)" />
                <unit name = "MOLE SI"          unit = "J/(mol * K)" />
                <unit name = "MASS SI"          unit = "J/(g * K)" />
                <unit name = "SI WITH C"        unit = "J/(g * K)" />

                <unit name = "MOLAR BASE SI"    unit = "J/(mol * K)" />
                <unit name = "MASS BASE SI"     unit = "J/(kg * K)" />
                <unit name = "ENGLISH"          unit = "BTU/(lbm * R)" />
                <unit name = "MOLAR ENGLISH"    unit = "BTU/(lbmol * R)" />

                <unit name = "MKS"              unit = "J/(g * K)" />
                <unit name = "CGS"              unit = "J/(g * K)" />
                <unit name = "MIXED"            unit = "J/(g * K)" />
                <unit name = "MEUNITS"          unit = "J/(g * K)" />

            </units>

        </refprop_name>
        <refprop_name name = "CV">

            <std_names>

                <std_name name="cv"/>
                <std_name name="isobaric_heat_capacity"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = "J/(mol * K)" />
                <unit name = "MOLE SI"          unit = "J/(mol * K)" />
                <unit name = "MASS SI"          unit = "J/(g * K)" />
                <unit name = "SI WITH C"        unit = "J/(g * K)" />

                <unit name = "MOLAR BASE SI"    unit = "J/(mol * K)" />
                <unit name = "MASS BASE SI"     unit = "J/(kg * K)" />
                <unit name = "ENGLISH"          unit = "BTU/(lbm * R)" />
                <unit name = "MOLAR ENGLISH"    unit = "BTU/(lbmol * R)" />

                <unit name = "MKS"              unit = "J/(g * K)" />
                <unit name = "CGS"              unit = "J/(g * K)" />
                <unit name = "MIXED"            unit = "J/(g * K)" />
                <unit name = "MEUNITS"          unit = "J/(g * K)" />

            </units>

        </refprop_name>
        <refprop_name name = "CP/CV">

            <std_names>

                <std_name name="gamma"/>
                <std_name name="cp/cv"/>
                <std_name name="heat_capacity_ratio"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = " - " />
                <unit name = "MOLE SI"          unit = " - " />
                <unit name = "MASS SI"          unit = " - " />
                <unit name = "SI WITH C"        unit = " - " />

                <unit name = "MOLAR BASE SI"    unit = " - " />
                <unit name = "MASS BASE SI"     unit = " - " />
                <unit name = "ENGLISH"          unit = " - " />
                <unit name = "MOLAR ENGLISH"    unit = " - " />

                <unit name = "MKS"              unit = " - " />
                <unit name = "CGS"              unit = " - " />
                <unit name = "MIXED"            unit = " - " />
                <unit name = "MEUNITS"          unit = " - " />

            </units>

        </refprop_name>
        <refprop_name name = "W">

            <std_names>

                <std_name name="c"/>
                <std_name name="sos"/>
                <std_name name="speed_of_sound"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = "m/s" />
                <unit name = "MOLE SI"          unit = "m/s" />
                <unit name = "MASS SI"          unit = "m/s" />
                <unit name = "SI WITH C"        unit = "m/s" />

                <unit name = "MOLAR BASE SI"    unit = "m/s" />
                <unit name = "MASS BASE SI"     unit = "m/s" />
                <unit name = "ENGLISH"          unit = "ft/s" />
                <unit name = "MOLAR ENGLISH"    unit = "ft/s" />

                <unit name = "MKS"              unit = "m/s" />
                <unit name = "CGS"              unit = "cm/s" />
                <unit name = "MIXED"            unit = "m/s" />
                <unit name = "MEUNITS"          unit = "cm/s" />

            </units>

        </refprop_name>
        <refprop_name name = "PRANDTL">

            <std_names>

                <std_name name="Pr"/>

            </std_names>
            <units>

                <unit name = "DEFAULT"          unit = " - " />
                <unit name = "MOLE SI"          unit = " - " />
                <unit name = "MASS SI"          unit = " - " />
                <unit name = "SI WITH C"        unit = " - " />

                <unit name = "MOLAR BASE SI"    unit = " - " />
                <unit name = "MASS BASE SI"     unit = " - " />
                <unit name = "ENGLISH"          unit = " - " />
                <unit name = "MOLAR ENGLISH"    unit = " - " />

                <unit name = "MKS"              unit = " - " />
                <unit name = "CGS"              unit = " - " />
                <unit name = "MIXED"            unit = " - " />
                <unit name = "MEUNITS"          unit = " - " />

            </units>

        </refprop_name>

    </names>
    <derivatives>

        <main_derivatives_prop>

            <refprop_name name = "P"/>
            <refprop_name name = "T"/>
            <refprop_name name = "D"/>

        </main_derivatives_prop>
        <other_derivatives_prop>

            <refprop_name name = "H"/>
            <refprop_name name = "S"/>

        </other_derivatives_prop>

    </derivatives>
    <unit_conversion>

        <unit_prop_name name = "P">

            <func name="multiply"   ext_qty_location="none"/>

            <units>
                <unit name = "kPa">
                    <factor name="mult" value="1"/>
                </unit>
                <unit name = "MPa">
                    <factor name="mult" value="1000"/>
                </unit>
                <unit name = "Pa">
                    <factor name="mult" value="0.001"/>
                </unit>
                <unit name = "bar">
                    <factor name="mult" value="100"/>
                </unit>
                <unit name = "psia">
                    <factor name="mult" value="6.894757293178"/>
                </unit>
            </units>

        </unit_prop_name>
        <unit_prop_name name = "T">

            <func name="sum_mult"   ext_qty_location="none"/>

            <units>
                <unit name = "K">
                    <factor name="sum" value="-273.15"/>
                    <factor name="mult" value="1"/>
                </unit>
                <unit name = "C">
                    <factor name="sum" value="0"/>
                    <factor name="mult" value="1"/>
                </unit>
                <unit name = "F">
                    <factor name="sum" value="-32"/>
                    <factor name="mult" value="0.5555555555555556"/>
                </unit>
            </units>

        </unit_prop_name>
        <unit_prop_name name = "D">

            <func name="multiply"   ext_qty_location="num"/>

            <units>

                <unit name = "kg/m^3">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" value="mass"/>
                </unit>
                <unit name = "g/cm^3">
                    <factor name="mult" value="1000"/>
                    <factor name="quantity" value="mass"/>
                </unit>
                <unit name = "lbm/ft^3">
                    <factor name="mult" value="16.018"/>
                    <factor name="quantity" value="mass"/>
                </unit>

                <unit name = "mol/dm^3">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" value="mol"/>
                </unit>
                <unit name = "mol/m^3">
                    <factor name="mult" value="0.001"/>
                    <factor name="quantity" value="mol"/>
                </unit>
                <unit name = "lbmol/ft^3">
                    <factor name="mult" value="16.018"/>
                    <factor name="quantity" value="mol"/>
                </unit>

            </units>

        </unit_prop_name>
        <unit_prop_name name = "E">

            <func name="multiply"   ext_qty_location="den"/>

            <units>

                <unit name = "J/g">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>
                <unit name = "J/kg">
                    <factor name="mult" value="0.001"/>
                    <factor name="quantity" value="mass"/>
                </unit>
                <unit name = "BTU/lbm">
                    <factor name="mult" value="2.326"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>

                <unit name = "J/mol">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" value="mol"/>
                </unit>
                <unit name = "BTU/lbmol">
                    <factor name="mult" value="2.326"/>
                    <factor name="quantity" pos="den" value="mol"/>
                </unit>

            </units>

        </unit_prop_name>
        <unit_prop_name name = "H">

            <func name="multiply"   ext_qty_location="den"/>

            <units>

                <unit name = "J/g">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>
                <unit name = "J/kg">
                    <factor name="mult" value="0.001"/>
                    <factor name="quantity" value="mass"/>
                </unit>
                <unit name = "BTU/lbm">
                    <factor name="mult" value="2.326"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>

                <unit name = "J/mol">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" value="mol"/>
                </unit>
                <unit name = "BTU/lbmol">
                    <factor name="mult" value="2.326"/>
                    <factor name="quantity" pos="den" value="mol"/>
                </unit>

            </units>

        </unit_prop_name>
        <unit_prop_name name = "S">

            <func name="multiply"   ext_qty_location="den"/>

            <units>

                <unit name = "J/(g * K)">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>
                <unit name = "J/(kg * K)">
                    <factor name="mult" value="0.001"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>
                <unit name = "BTU/(lbm * R)">
                    <factor name="mult" value="4.1868"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>

                <unit name = "J/(mol * K)">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" pos="den" value="mol"/>
                </unit>
                <unit name = "BTU/(lbmol * R)">
                    <factor name="mult" value="4.1868"/>
                    <factor name="quantity" pos="den" value="mol"/>
                </unit>

            </units>

        </unit_prop_name>
        <unit_prop_name name = "Q">

            <func name="none"   ext_qty_location="none"/>

        </unit_prop_name>
        <unit_prop_name name = "VIS">

            <func name="multiply"   ext_qty_location="none"/>

            <units>

                <unit name = "uPa * s">
                    <factor name="mult" value="0.000001"/>
                </unit>
                <unit name = "Pa * s">
                    <factor name="mult" value="1"/>
                </unit>
                <unit name = "lbm/(ft * s)">
                    <factor name="mult" value="1.4882"/>
                </unit>
                <unit name = "cpoise">
                    <factor name="mult" value="0.001"/>
                </unit>

            </units>

        </unit_prop_name>
        <unit_prop_name name = "TCX">

            <func name="multiply"   ext_qty_location="none"/>

            <units>

                <unit name = "W/(m * K)">
                    <factor name="mult" value="1"/>
                </unit>
                <unit name = "mW/(m * K)">
                    <factor name="mult" value="0.001"/>
                </unit>
                <unit name = "BTU/(h * ft * R)">
                    <factor name="mult" value="1.730735"/>
                </unit>

            </units>

        </unit_prop_name>
        <unit_prop_name name = "CP">

            <func name="multiply"   ext_qty_location="den"/>

            <units>

                <unit name = "J/(g * K)">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>
                <unit name = "J/(kg * K)">
                    <factor name="mult" value="0.001"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>
                <unit name = "BTU/(lbm * R)">
                    <factor name="mult" value="4.1868"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>

                <unit name = "J/(mol * K)">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" pos="den" value="mol"/>
                </unit>
                <unit name = "BTU/(lbmol * R)">
                    <factor name="mult" value="4.1868"/>
                    <factor name="quantity" pos="den" value="mol"/>
                </unit>

            </units>

        </unit_prop_name>
        <unit_prop_name name = "CP0">

            <func name="multiply"   ext_qty_location="den"/>

            <units>

                <unit name = "J/(g * K)">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>
                <unit name = "J/(kg * K)">
                    <factor name="mult" value="0.001"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>
                <unit name = "BTU/(lbm * R)">
                    <factor name="mult" value="4.1868"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>

                <unit name = "J/(mol * K)">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" pos="den" value="mol"/>
                </unit>
                <unit name = "BTU/(lbmol * R)">
                    <factor name="mult" value="4.1868"/>
                    <factor name="quantity" pos="den" value="mol"/>
                </unit>

            </units>

        </unit_prop_name>
        <unit_prop_name name = "CV">

            <func name="multiply"   ext_qty_location="den"/>

            <units>

                <unit name = "J/(g * K)">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>
                <unit name = "J/(kg * K)">
                    <factor name="mult" value="0.001"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>
                <unit name = "BTU/(lbm * R)">
                    <factor name="mult" value="4.1868"/>
                    <factor name="quantity" pos="den" value="mass"/>
                </unit>

                <unit name = "J/(mol * K)">
                    <factor name="mult" value="1"/>
                    <factor name="quantity" pos="den" value="mol"/>
                </unit>
                <unit name = "BTU/(lbmol * R)">
                    <factor name="mult" value="4.1868"/>
                    <factor name="quantity" pos="den" value="mol"/>
                </unit>

            </units>

        </unit_prop_name>
        <unit_prop_name name = "CP/CV">

            <func name="none"   ext_qty_location="none"/>

        </unit_prop_name>
        <unit_prop_name name = "W">

            <func name="multiply"   ext_qty_location="none"/>

            <units>

                <unit name = "m/s">
                    <factor name="mult" value="1"/>
                </unit>
                <unit name = "ft/s">
                    <factor name="mult" value="0.3048"/>
                </unit>
                <unit name = "cm/s">
                    <factor name="mult" value="0.01"/>
                </unit>

            </units>

        </unit_prop_name>
        <unit_prop_name name = "PRANDTL">

            <func name="none"   ext_qty_location="none"/>

        </unit_prop_name>

    </unit_conversion>

</data>

""".format(fileversion=FILE_VERSION)

def generate_rp_name_file():

    rp_names_path = os.path.join(__CURR_DIR, "REFPROP_names.xml")

    with open(rp_names_path, "w") as file:

        file.write(__RP_NAMES_TXT)