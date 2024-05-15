c = get_config()
c.ClearHiddenTests.begin_test_delimeter = "THIS IS SPARTA!"
c.ClearHiddenTests.end_test_delimeter = "UPS... THIS IS NOT SPARTA"
c.LockCells.lock_all_cells = True
c.LockCells.lock_grade_cells = True
c.LockCells.lock_readonly_cells = True
c.LockCells.lock_solution_cells = True
c.ExecutePreprocessor.interrupt_on_timeout = True
c.ExecutePreprocessor.timeout = 300
c.ClearSolutions.code_stub = {
"R": "# your R code here\n# end of R code\n",
"python": "# your python code here\n# end of python code\n",
"ruby": "# your ruby code here            \n# end of ruby code"
}
