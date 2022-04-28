def pytest_html_report_title(report):
    report.title = "Pokemon tests suite"

def pytest_configure(config):
    config.option.htmlpath = '../reports/report.html'
