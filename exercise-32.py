bal = 100  # bal:100, inter:none, withDr:none
inter = .05  # bal:100, inter:0.05, withDr:none
withDr = 25  # bal:100, inter:0.05, withDr:25
bal += (inter * bal)  # bal:105.0, inter:0.05, withDr:25
bal = bal - withDr  # bal:80, inter:0.05, withDr:25