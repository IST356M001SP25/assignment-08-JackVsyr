import pandas as pd
import streamlit as st 


def top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    ABLdf = violations_df.pivot_table(index='location', values='amount', aggfunc='sum').sort_values(by='amount', ascending=False)
    ABLdf['location'] = ABLdf.index
    ABLdf.reset_index(drop=True, inplace=True)
    return ABLdf[ABLdf['amount'] >= threshold]


def top_locations_mappable(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    TLdf = top_locations(violations_df, threshold)
    violations_old_df = violations_df[['location', 'lat', 'lon']].drop_duplicates(subset=['location'])
    merged_df = pd.merge(TLdf, violations_old_df, on='location')
    return merged_df.drop_duplicates()

def tickets_in_top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    TLdf = top_locations(violations_df)
    merged_df = pd.merge(TLdf[['location']], violations_df, on='location')
    return merged_df

if __name__ == '__main__':
    '''
    Main ETL job. 
    '''
    print("Running job...")
    print("Reading violations from cache/final_cuse_parking_violations.csv")

    violations_df = pd.read_csv('/Users/jack/Downloads/IST 356/assignment-08-JackVsyr/cache/final_cuse_parking_violations.csv')
    TL_df = top_locations(violations_df)
    print("Writing top locations to cache/top_locations.csv")
    TL_df.to_csv('/Users/jack/Downloads/IST 356/assignment-08-JackVsyr/cache/top_locations.csv', index=False)
    
    TL_map_df = top_locations_mappable(violations_df)

    print("Writing mappable top locations to cache/top_locations_mappable.csv")
    TL_map_df.to_csv('/Users/jack/Downloads/IST 356/assignment-08-JackVsyr/cache/top_locations_mappable.csv', index=False)

    tickets_in_TL_df = tickets_in_top_locations(violations_df, TL_df)

    print("Writing tickets in top locations to cache/tickets_in_top_locations.csv")
    tickets_in_TL_df.to_csv('/Users/jack/Downloads/IST 356/assignment-08-JackVsyr/cache/tickets_in_top_locations.csv', index=False)