import os
import h5py
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

def extract_mcdc_results(mcdc_dir):
    results = {}
    for file in os.listdir(mcdc_dir):
        if file.endswith(".h5"):
            file_path = os.path.join(mcdc_dir, file)
            print("Extracting MC/DC results from:", file_path)
            try:
                with h5py.File(file_path, 'r') as f:
                    k_mean = np.array(f["k_mean"])
                    k_sdev = np.array(f["k_sdev"])
                    print(k_mean)
                    if k_mean is not None and k_sdev is not None:
                        problem_name = file.replace(".h5", "")
                        results[problem_name] = {"mcdc_k_mean": k_mean, "mcdc_k_sdev": k_sdev}
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    return results

def extract_openmc_results(openmc_dir):
    results = {}
    parent_dir = os.path.basename(os.path.dirname(openmc_dir))
    case_dirs = [os.path.join(openmc_dir, d) for d in os.listdir(openmc_dir) if d.startswith("case-") and os.path.isdir(os.path.join(openmc_dir, d))]
    
    if not case_dirs:
        case_dirs = [openmc_dir]  # If no case-# subdirectories, use openmc_dir itself
    
    for case_dir in case_dirs:
        stdout_file = os.path.join(case_dir, "openmc.stdout")
        if os.path.exists(stdout_file):
            print("Extracting openmc results from:", case_dir)
            try:
                with open(stdout_file, 'r') as f:
                    for line in f:
                        match = re.search(r'Combined k-effective\s+=\s+([\d\.]+)\s+\+/-\s+([\d\.]+)', line)
                        if match:
                            k_mean = float(match.group(1))
                            k_sdev = float(match.group(2))
                            case_name = os.path.basename(case_dir) if "case-" in case_dir else ""
                            problem_name = f"{parent_dir}_{case_name}" if case_name else parent_dir
                            results[problem_name] = {"openmc_k_mean": k_mean, "openmc_k_sdev": k_sdev}
                            break  # Stop after finding the first match
            except Exception as e:
                print(f"Error reading {stdout_file}: {e}")
    return results

def collect_results1(root_dir):
    dataset = {}
    
    for dirpath, dirnames, _ in os.walk(root_dir):
        if "mcdc" in dirnames:
            mcdc_results = extract_mcdc_results(os.path.join(dirpath, "mcdc"))
            dataset.update(mcdc_results)
        if "openmc" in dirnames:
            openmc_results = extract_openmc_results(os.path.join(dirpath, "openmc"))
            dataset.update(openmc_results)
    df = pd.DataFrame.from_dict(dataset, orient='index').reset_index().rename(columns={'index': 'problem_name'})
    df.to_csv("results_summary.csv", index=False)
    print("Results collected and saved to results_summary.csv")

def collect_results(root_dir):
    dataset = {}

    for dirpath, dirnames, _ in os.walk(root_dir):
        if "mcdc" in dirnames:
            mcdc_results = extract_mcdc_results(os.path.join(dirpath, "mcdc"))
            for problem_name, values in mcdc_results.items():
                if problem_name not in dataset:
                    dataset[problem_name] = {}
                dataset[problem_name].update(values)

        if "openmc" in dirnames:
            openmc_results = extract_openmc_results(os.path.join(dirpath, "openmc"))
            for problem_name, values in openmc_results.items():
                if problem_name not in dataset:
                    dataset[problem_name] = {}
                dataset[problem_name].update(values)

    # Convert to DataFrame and ensure all columns exist
    df = pd.DataFrame.from_dict(dataset, orient='index').reset_index().rename(columns={'index': 'problem_name'})

    # Ensure all columns exist, filling missing values with NaN
    expected_columns = ["problem_name", "openmc_k_mean", "openmc_k_sdev", "mcdc_k_mean", "mcdc_k_sdev"]
    df = df.reindex(columns=expected_columns)

    # Save to CSV
    df.to_csv("results_summary.csv", index=False)
    print("Results collected and saved to results_summary.csv")

#root_directory = os.getcwd()  # Start search from current directory
#collect_results(root_directory)




### plotting
plotting_toggle = 1

def plot_icsbep_comparison(df, title):

    # Set up the plot
    plt.figure(figsize=(12, 6))
    x_labels = df["problem_name"]
    x = np.arange(len(x_labels))  # Create x positions for labels

    # Plot OpenMC and MCDC k_mean values
    plt.scatter(x, df["openmc_k_mean"], marker='o',  label="OpenMC" , color='b')
    plt.errorbar(x, df["openmc_k_mean"], yerr=df["openmc_k_sdev"], fmt='o', color='b', capsize=3)
    plt.scatter(x, df["mcdc_k_mean"], marker='s', label="MC/DC", color='r')
    plt.errorbar(x, df["mcdc_k_mean"], yerr=df["mcdc_k_sdev"], fmt='o', color='r', capsize=3)

    # Format the x-axis for better readability
    plt.xticks(x, x_labels, rotation=45, ha="right", fontsize=8)  # Rotate labels
    #plt.xlabel("Problem Name")
    plt.ylabel("keff")
    plt.title(title)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

# Load the CSV file
df = pd.read_csv("results_summary.csv")
df = df[:118]

df_heu_met_fast = df[:25]
df_heu_sol_therm = df[25:44]
df_misc = pd.concat([df[44:48], df[56:57], df[117:118]])
df_leu_sol_therm = df[48:56]
df_pu_met_fast = df[57:64]
df_pu_sol_therm = df[64:108]
df_u233_met_fast = df[108:117]

if plotting_toggle == 1:
    plot_icsbep_comparison(df_heu_met_fast, "ICSBEP: HEU-MET-FAST")
    plot_icsbep_comparison(df_heu_sol_therm, "ICSBEP: HEU-SOL-THERM")
    plot_icsbep_comparison(df_misc, "ICSBEP: Miscellaneous")
    plot_icsbep_comparison(df_leu_sol_therm, "ICSBEP: LEU-SOL-THERM")
    plot_icsbep_comparison(df_pu_met_fast, "ICSBEP: PU-MET-FAST")
    plot_icsbep_comparison(df_pu_sol_therm, "ICSBEP: PU-SOL-THERM")
    plot_icsbep_comparison(df_u233_met_fast, "ICSBEP: U233-MET-FAST")

