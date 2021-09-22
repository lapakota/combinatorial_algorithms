<?php

function parse_file($filename): array
{
    $str = htmlentities(file_get_contents($filename));
    return array_map('intval', explode(' ', str_replace("\r\n", " ", $str)));
}

function arr_to_list($adj_arr): array
{
    $adj_list = array(array());
    $vertex_number = 1;
    while ($adj_arr[$vertex_number] != $adj_arr[0]) {
        for ($i = $adj_arr[$vertex_number]; $i < $adj_arr[$vertex_number + 1]; $i += 2) {
            $adj_list[$vertex_number - 1][$adj_arr[$i] - 1] = $adj_arr[$i + 1];
        }
        $vertex_number++;
    }
    return $adj_list;
}

function find_min_route($visited, $adj_list): array
{
    $min_weight = 32767;
    $from_vert = -1;
    $to_vert = -1;

    foreach ($visited as $vertex) {
        foreach ($adj_list[$vertex] as $key => $value) {
            if ($value < $min_weight && !in_array($key, $visited)) {
                $min_weight = $value;
                $from_vert = $vertex;
                $to_vert = $key;
            }
        }
    }
    return array($from_vert, $to_vert, $min_weight);
}

function mst_route_to_list($mst_route): array
{
    $mst_adj_list = array();

    foreach ($mst_route as $arr) {
        foreach ($arr as $key => $value) {
            if (!array_key_exists($key, $mst_adj_list)) {
                $mst_adj_list[$key] = array();
            }
            if (!array_key_exists($value, $mst_adj_list)) {
                $mst_adj_list[$value] = array();
            }
            array_push($mst_adj_list[$key], $value);
            array_push($mst_adj_list[$value], $key);
        }
    }

    return $mst_adj_list;
}

function prims_algorithm($adj_list): array
{
    $mst_route = array();
    $visited = array(0);
    $weight = 0;

    for ($i = 0; $i < count($adj_list) - 1; $i++) {
        $raw_data = find_min_route($visited, $adj_list);
        $from_vert = $raw_data[0];
        $to_vert = $raw_data[1];
        $weight += $raw_data[2];
        array_push($visited, $to_vert);
        array_push($mst_route, array($from_vert => $to_vert));
    }
    return array(mst_route_to_list($mst_route), $weight);
}

function write_to_file($mst_list, $weight)
{
    $output_string = '';
    ksort($mst_list);
    foreach ($mst_list as $arr) {
        asort($arr);
        $output_string .= implode(' ', array_map(function($n){return ++$n;}, $arr)) . " 0\n";
    }
    $output_string .= $weight;
    //print_r($output_string);
    file_put_contents('out.txt', $output_string);
}

function main()
{
    $adj_list = arr_to_list(parse_file('in.txt'));

    $raw_data = prims_algorithm($adj_list);
    $mst = $raw_data[0];
    $weight = $raw_data[1];

    write_to_file($mst, $weight);
}

main();