def melting_temp(sequence):
    a_t_count = sequence.count ("A") + sequence.count ("T")
    g_c_count = sequence.count ('G') + sequence.count ('T')
    melt = 4 * (g_c_count) + 2 * (a_t_count)
    return melting_temp


