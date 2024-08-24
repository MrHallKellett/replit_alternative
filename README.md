# replit_alternative

Some tools to help deal with replit's announcement that they are deprecating their Teams for Edu service.

## scrape_io_tests.py

A script that automates the process of exporting I/O tests from assignments (as these currently cannot be exported without clicking through every single test individually)

![Demo of I/O test scraping](assets/replit_io_tests_export.gif)

## tests.py

Run replit I/O tests locally using `unittest.mock.patch`.

![Demo of I/O test running](assets/replit_io_test_runner.gif)

## aggregate_test_results.py

Iterate through student test case files and aggregate results.

Generate progress report in HTML format.

![Test Result Report](assets/test_result_report.png)