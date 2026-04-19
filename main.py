from config import API_KEY, SYMBOLS, OUTPUT_RAW_PATH, OUTPUT_PROCESSED_PATH
from extract import fetch_stock_data
from transform import transform_data
from load import save_to_csv, save_to_postgres, load_dim_stock

def run_pipeline():
    print("Starting pipeline...")

   
    # EXTRACT
    
    raw_data = fetch_stock_data(API_KEY, SYMBOLS)
    print("Extraction completed")

   
    # SAVE RAW DATA
   
    save_to_csv(raw_data, OUTPUT_RAW_PATH)

    
    # TRANSFORM
   
    processed_data = transform_data(raw_data)
    print("Transformation completed")

    
    #SAVE PROCESSED DATA
   
    save_to_csv(processed_data, OUTPUT_PROCESSED_PATH)

    
    # LOAD TO POSTGRES (FACT TABLE)
    
    save_to_postgres(processed_data, "fact_stock_prices")

  
    # LOAD DIMENSION TABLE
   
    load_dim_stock()

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()