require"splay.base"
local log = require"splay.log"
local l_o = log.new(3, "[test_events_periodic]")
e={}
ITERATIONS=5
events.run(function()
	events.thread(function()
		l_o:print("waiting for 'op' event")
		events.wait("op")
		assert(#e==ITERATIONS)
		print("TEST_OK")
		events.exit()
	end)
	events.periodic(1, function()
		e[#e+1]="op"		
		if #e==ITERATIONS then 
			l_o:print("Periodic thread did "..ITERATIONS..", firing 'op'")
			events.fire("op")
		end
	end)
end)