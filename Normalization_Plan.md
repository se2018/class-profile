# Normalizing the data

## Goal

The goal of normalizing the data is to make all of the data consistent and
easy to be processed afterwards by a computer program. This is the first
step to processing the data.

## Process

There are five steps to the process.
1. Patrick runs a script that takes all of the entries in a column, shuffles the order, and then exports the shuffled rows as well as a mapping of the orders.
2. The shuffled rows are stored in a shared folder, and the mapping is kept private.
3. On our end, we download the shuffled rows, and manually go through each one to ensure that they’re normalized.
4. Once we’ve finalized the shuffled rows, we transfer back the verified shuffled rows to the shared folder.
5. We sort the shuffled rows back to their original row number using the private original mapping that was saved.

Note: This process isn't fool proof. To save any work, you can store the git
project in Dropbox/Google Drive.

### Step One: Create rows

You can find the normalization script in `utils/Data Normalization.ipynb`.
Running this script will grab the dataset filename `raw_file` and create two files for each
column to normalize. The path to the `raw_file` can be modified, depending on
where you stored the raw file. Do NOT check in the raw file into git.

The columns that will be normalized are defined within `constants.py`. It will
store all of the shuffled rows into `rows_output_directory` and the shuffled
indices into `indices_output_directory`.

### Step Two: Share the rows

Only the `rows_output_directory` should be shared with the team that will be
normalizing the data. Once shared, we'll download the folder into the same path,
and normalize all of the data by hand.

### Step Three: Normalize the data

For each column, we'll need to standardize the way we want to process the data.
In order to avoid too much work, we'll just have each column assigned to one
person, rather than split a column, and let that person decide how that column
should be normalized in a way that can easily be programmatically processed.

### Step Four: Share the normalized data

We share the folder containing all of the normalized columns to Patrick. Patrick
then places the normalized rows folder into the same path as the
`normalized_rows_directory` variable in the `utils/Flush Normalized Data.ipynb`
file.

### Step Five: Flush the data into the data set

This can be done using `utils/Flush Normalized Data.ipynb`. This script will use
the hidden indices files to write all of the normalized columns into the
dataset. In order to preserve a history of the files in case we need to do this
multiple times, the filename is suffixed with the date i.e. `results-02-19.csv`.

## Why this process is secure

The only way to identify someone is to look at unique values that can identify
someone. Once the row is identified as belonging to someone, it becomes easy to
read the entire row and learn all of their private information. For example, if
I know that Bob was the only one who worked at Hooli, then I look for Hooli,
identify the row, and read all of Bob's personal info.

By disconnecting all of the column values from each other and shuffling them all
individually, it becomes impossible to connect which data belongs to who. This
is because each file contains all of the rows value for one column, and is
shuffled differently compared to every other file. As a result, even if I know X
is the row for Bob, it doesn't mean that the Xth row for another file is Bob's.
Without the indices file, it's impossible to confirm which values belong to Bob.

I'm almost positive that it's safe to publish all of the individual rows on
GitHub. But there's no point in doing that so we won't do that.
