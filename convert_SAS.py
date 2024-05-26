
import pandas as pd

def convert_sas(prefix="t1"):
    df = pd.read_clipboard(sep="\t")
    df.Label = df.Label.fillna(df.Name)
    df.loc[df['Type'] == 'Character', 'Type'] = '$'
    df.loc[df['Type'] == 'Currency', 'Type'] = 'Dollar'
    df.loc[df['Type'] == 'Numeric', 'Type'] = ''
    df.loc[df['Type'] == 'Date', 'Type'] = 'Date'
    df["NFormat"] = df["Type"] + df["Length"].astype(str) + "."
    df['select'] = prefix + '.' + df['Name'] + " format=" + df['NFormat'] \
        + " Label='" + df['Label'] + "',"
    data = df.drop(columns=["Name", "Type", "Length", "Format", "NFormat",
                            "Informat", "Label"])
    data.to_clipboard(index=False)
    print(data)

convert_sas()

