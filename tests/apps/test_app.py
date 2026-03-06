def test_importing_app():
    # this will raise an exception if pydantic model validation fails for the app
    from aifparser.apps import aif_app_entry_point

    assert aif_app_entry_point.app.label == 'AIF'
