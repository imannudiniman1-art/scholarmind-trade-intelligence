def assess_risk(risk):
    """
    Assess trade risk level.

    Risk score:
    0-29   = Low
    30-59  = Medium
    60+    = High
    """
    if risk < 30:
        return "Low Risk"
    elif risk < 60:
        return "Medium Risk"
    else:
        return "High Risk"