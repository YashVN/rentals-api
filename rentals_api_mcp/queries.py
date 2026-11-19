from pathlib import Path 
import sqlite3

DB_PATH = Path(__file__).resolve().parent.parent/"telemetry.db"

def percentile(values:list[float],pct;float)->float:
    """
    Nearest rank percentiles
    """
    if not values: 
        return 0.0 

    ordered = sorted(values)
    index = max(0,min(len(ordered)-1,round(pct/100*len(ordered))-1))
    return round(ordered[index]-1)
