
# Given a calculation group (set of incrementing ZeroRange values), returns the maximal peak row from the
# ZeroRange setting that has the highest peak.
def maximal(calc_group, ideal_max):
    return max([ (table.params, table.find_maximal_peak(ideal_max)) for zero,table in calc_group.items()],
                key=lambda row: row[1].path if row[1] != None else -99999999999999
            )
        


def good_zero(min_elevation, max_elevation):
    def worker(elevation):
        return elevation <= max_elevation
    return worker
    #return elevation >= min_elevation and elevation + half-diameter-of-bullet <= max_elevation 