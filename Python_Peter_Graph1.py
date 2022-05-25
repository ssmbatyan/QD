import onetick.query as otq
import onetick.core as otc

def configure_query_for_Graph_1(query):
	query.set_start_time(otc.timeval_t(1070236800, 0)).set_end_time(otc.timeval_t(1070323200, 0))
	tip = otc.TimeIntervalProperties()
	tip.set_timezone('WET')
	query.set_time_interval_properties(tip)
	query_props = otc.QueryProperties()
	query.set_query_properties(query_props)
	query.set_symbols([otq.Symbol('DEMO_L1::A', {})])
	query.set_query_name('Graph_1')

@otq.query_creator
def Graph_1():
	join_by_time_1 = otq.JoinByTime()
	join_by_time_1.set_output_pin_name(output_name='', pin_name='OUT')
	compute_1 = otq.Compute(compute='SUM')
	compute_1.set_node_name('trd_sum')
	compute_2 = otq.Compute(compute='SUM')
	compute_2.set_node_name('trd_by_day')
	passthrough_1 = otq.Passthrough().set_tick_types(['TRD'])
	passthrough_1.set_input_pin_name(input_name='', pin_name='IN')
	compute_3 = otq.Compute(compute='SUM')
	compute_3.set_node_name('trd')
	compute_4 = otq.Compute(compute='SUM')
	compute_4.set_node_name('trd')
	compute_5 = otq.Compute(compute='SUM')
	compute_5.set_node_name('qte_sum')
	compute_6 = otq.Compute(compute='SUM')
	compute_6.set_node_name('qte_by_day')
	passthrough_2 = otq.Passthrough().set_tick_types(['TRD'])
	passthrough_2.set_input_pin_name(input_name='', pin_name='IN_1')
	compute_7 = otq.Compute(compute='SUM')
	compute_7.set_node_name('qte')
	compute_8 = otq.Compute(compute='SUM')
	compute_8.set_node_name('qte')

	chain_0 = passthrough_1 >> otq.Chainlet(compute_2, compute_1)
	chain_0 >> join_by_time_1
	chain_1 = passthrough_1 >> otq.Chainlet(compute_4, compute_3)
	chain_1 >> join_by_time_1
	chain_2 = passthrough_2 >> otq.Chainlet(compute_6, compute_5)
	chain_2 >> join_by_time_1
	chain_3 = passthrough_2 >> otq.Chainlet(compute_8, compute_7)
	chain_3 >> join_by_time_1
	graph = otq.Graph(join_by_time_1)
	query = otq.Query(graph)
	configure_query_for_Graph_1(query)
	query_params = {}
	query.set_query_params(query_params)
	return query
	
def configure_query_for_Graph_2(query):
	query.set_start_time(otc.timeval_t(1070254800, 0)).set_end_time(otc.timeval_t(1070341200, 0))
	tip = otc.TimeIntervalProperties()
	tip.set_timezone('America/New_York')
	query.set_time_interval_properties(tip)
	query_props = otc.QueryProperties()
	query.set_query_properties(query_props)
	query.set_symbols([otq.Symbol('DEMO_L1::A', {})])
	query.set_query_name('Graph_2')

@otq.query_creator
def Graph_2():
	passthrough_1 = otq.Passthrough().set_tick_types(['TRD'])
	passthrough_1.set_input_pin_name(input_name='', pin_name='IN')
	passthrough_1.set_output_pin_name(output_name='', pin_name='OUT')
	graph = otq.Graph(passthrough_1)
	query = otq.Query(graph)
	configure_query_for_Graph_2(query)
	query_params = {}
	query.set_query_params(query_params)
	return query

