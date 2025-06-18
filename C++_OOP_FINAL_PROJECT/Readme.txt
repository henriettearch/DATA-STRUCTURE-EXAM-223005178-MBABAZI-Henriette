 My project was about ATM Cash Dispenser, C++ Project

What This Project Does

This project simulates how a real ATM machine dispenses cash based on the amount entered by a user. It uses two different algorithms to give out money:

Greedy Method: Dispenses the highest denominations first (e.g., $100 before $50) to quickly cover the amount.

Optimal Method: Dispenses notes in such a way that the total number of notes given is minimized, even if it means using smaller denominations.

The ATM machine operates with fixed denominations: $100, $50, $20, and $10.

How I Made It:

I developed the program using C++ programming language.

A custom Denomination structure is used to store note values and track how many are available.

I created two classes for the cash dispensers:

One class implements the Greedy Dispenser.

Another class implements the Optimal Dispenser using algorithmic logic for minimal notes.

I used dynamic memory (new and delete) to manage memory manually, simulating the way real-world ATM systems track and update cash in real time.

How It Works

The program starts by loading the ATM with 10 notes of each denomination ($100, $50, $20, and $10).

The user is prompted to enter an amount they wish to withdraw.

The program then:

Tries to dispense the amount using the Greedy Method.

Then tries again using the Optimal Method for the same amount.

It displays the number and types of notes dispensed in each case.

How to Run It
Copy and paste the code into any C++ compiler (such as Code::Blocks or an online compiler like repl.it).

Compile and run the program.

When prompted, enter the withdrawal amount (must be a multiple of 10).

View how the cash is dispensed using both methods.

Example Output
If you enter:

Enter amount to dispense: 180
The output will look like:

[Greedy Dispenser] Dispensing $180...
Dispensed 1 x $100
Dispensed 1 x $50
Dispensed 1 x $20
Dispensed 1 x $10

[Optimal Dispenser] Dispensing $180 (minimal notes)...
Dispensed 1 x $100
Dispensed 1 x $50
Dispensed 1 x $20
Dispensed 1 x $10

Cleaning Up:

After dispensing, the program releases all memory manually using delete to avoid memory leaks and simulate real ATM memory management processes.

Why This Project is Useful

It demonstrates how ATMs intelligently decide how to give out cash.

It combines object-oriented programming, algorithm design, and dynamic memory handling.

It deepens understanding of structures, classes, greedy vs. optimal algorithms, sorting techniques, and resource management.

It also gives practical insight into real-world applications of C++ in financial systems.



About how my codes works, let me go through it:

#include <iostream> : for including inputs and outputs
#include <algorithm>: for storing arrays

using namespace std; //to avoid many lines in your codes

// Structure to hold denomination value and its count
struct Denomination {
    int value;
    int* count; // pointer to hold dynamic count
};


// Global dynamic array of denominations
Denomination* denoms = nullptr;
int denomCount = 0;

// Function to add a new denomination or update existing one
(void addDenomination(int value, int count) {
    // If denomination already exists, just add the count
    for (int i = 0; i < denomCount; ++i) {
        if ((denoms + i)->value == value) {
            *(denoms[i].count) += count;
            return;
        }
    }): this function called addDenominator was created to add new denomination or for updating the exixting one

    // Create new array with space for new denomination
    (Denomination* newArr = new Denomination[denomCount + 1];
    for (int i = 0; i < denomCount; ++i)
        *(newArr + i) = *(denoms + i);

    // Add the new denomination at the end
    newArr[denomCount].value = value;
    newArr[denomCount].count = new int(count);

    // Replace old array with new one
    delete[] denoms;
    denoms = newArr;
    ++denomCount;
}) : this array called Denom was crated to hold or store new denomination at the end

// Function to remove a denomination by value
(void removeDenomination(int value) {
    int index = -1;

    // Find index of the denomination
    for (int i = 0; i < denomCount; ++i) {
        if ((denoms + i)->value == value) {
            index = i;
            break;
        }
    }) 
this function called removeDenomination was created so that it will help to find the index of denomination with specific value to be removed.

    // If not found, return
    if (index == -1) return;

    // Create new array without the removed denomination
    Denomination* newArr = new Denomination[denomCount - 1];
    for (int i = 0, j = 0; i < denomCount; ++i) {
        if (i == index) {
            delete denoms[i].count; // free memory
            continue;
        }
        *(newArr + j++) = *(denoms + i);
    }

    // Replace old array with new one
    delete[] denoms;
    denoms = newArr;
    --denomCount;
}
from where i created this function called removeDenomination these are the explaination of what is being done:
(This removeDenomination function removes a specific denomination (by its value) from the denoms array by:

-Searching for the index of the denomination with the given value.

-Returning early if not found (index == -1).

-Creating a new array with one less slot to exclude the denomination to be removed.

-Copying all other denominations into the new array.

-Freeing memory for the count of the removed denomination.

-Replacing the old array with the new one.

-Decreasing the total count of denominations.)

// Abstract class for cash dispenser
class CashDispenser {
public:
    virtual bool dispense(int amount) = 0; // pure virtual method
    virtual ~CashDispenser() {}
};

// Dispenses using greedy algorithm (largest to smallest)
(class GreedyDispenser : public CashDispenser {
public:
    bool dispense(int amount) override {
        cout << "\n[Greedy Dispenser] Dispensing $" << amount << "...\n";

        // Backup current counts in case we need to refund
        int* temp = new int[denomCount];
        for (int i = 0; i < denomCount; ++i)
            temp[i] = *(denoms + i)->count;

        // Sort denominations in descending order
        sort(denoms, denoms + denomCount, [](const Denomination& a, const Denomination& b) {
            return a.value > b.value;
        });

        int remaining = amount;

        // Try to use the largest denominations first
        for (int i = 0; i < denomCount && remaining > 0; ++i) {
            Denomination* d = denoms + i;
            int num = min(*(d->count), remaining / d->value);
            remaining -= num * d->value;
            *(d->count) -= num;

            // Output what we dispensed
            if (num > 0)
                cout << "Dispensed " << num << " x $" << d->value << "\n";
        }

 // If we couldn't dispense full amount, restore original state
        if (remaining > 0) {
            cout << "Unable to dispense full amount. Refunding.\n";
            for (int i = 0; i < denomCount; ++i)
                *(denoms + i)->count = temp[i];
            delete[] temp;
            return false;
        }

        delete[] temp;
        return true;
    }
};) from where we created class GreedyDispenser which is a child class from cashDispenser, it was created to define the GreedyDispenser class, 
which uses the greedy algorithm to give out cash starting with the biggest notes first.
It also tries to cover the amount using the largest available denominations and reduces the count of each note used.
If it can't give the full amount, it restores the original state and cancels the transaction.

// Dispenses using optimal strategy (minimum number of notes)
(class OptimalDispenser : public CashDispenser {
public:
    bool dispense(int amount) override {
        cout << "\n[Optimal Dispenser] Dispensing $" << amount << " (minimal notes)...\n";

        int minNotes = INT_MAX;
        int* bestUsed = new int[denomCount]{}; // best note usage
        bool found = false;

        // Try all combinations using backtracking
        backtrack(0, amount, 0, new int[denomCount]{}, bestUsed, minNotes, found);

        // If no solution found
        if (!found) {
            cout << "Unable to dispense full amount.\n";
            delete[] bestUsed;
            return false;
        }

        // Dispense the best combination found
        for (int i = 0; i < denomCount; ++i) {
            if (bestUsed[i] > 0) {
                *(denoms + i)->count -= bestUsed[i];
                cout << "Dispensed " << bestUsed[i] << " x $" << (denoms + i)->value << "\n";
            }
        }

        delete[] bestUsed;
        return true;
    }

private:
    // Recursive function to find the best combination (backtracking)
    void backtrack(int idx, int remaining, int usedNotes, int* used,
                   int* bestUsed, int& minNotes, bool& found) {
        // If exact amount is matched
        if (remaining == 0) {
            if (usedNotes < minNotes) {
                for (int i = 0; i < denomCount; ++i)
                    bestUsed[i] = used[i];
                minNotes = usedNotes;
                found = true;
            }
            return;
        }

        // If we've checked all denominations
        if (idx >= denomCount) return;

        Denomination* d = denoms + idx;
        int maxUse = min(*(d->count), remaining / d->value);

        // Try all possible counts of current denomination
        for (int i = maxUse; i >= 0; --i) {
            used[idx] = i;
            backtrack(idx + 1, remaining - i * d->value, usedNotes + i, used, bestUsed, minNotes, found);
        }

        used[idx] = 0; // reset for other paths
    }
};)
From where i created class called optimalDispenser to here, this class tries to give out cash using the smallest number of notes possible. 
It uses a backtracking method to test all combinations of available notes until it finds the best one that matches the requested amount. 
If it finds a solution, it dispenses the notes accordingly; otherwise, it shows that it cannot dispense the full amount.

int main() {
    cout << "=== ATM Cash Dispenser ===\n";

    // Initialize available denominations
    addDenomination(100, 10);
    addDenomination(50, 10);
    addDenomination(20, 10);
    addDenomination(10, 10);

    // Create both greedy and optimal dispensers
    int machineCount = 2;
    CashDispenser** machines = new CashDispenser*[machineCount];
    machines[0] = new GreedyDispenser();
    machines[1] = new OptimalDispenser();

    // Ask user how much money to dispense
    int amount;
    cout << "\nEnter amount to dispense: ";
    cin >> amount;

    // Try dispensing with both machines
    for (int i = 0; i < machineCount; ++i) {
        machines[i]->dispense(amount);
        cout << "-----------------------------\n";
    }

    // Clean up memory
    for (int i = 0; i < machineCount; ++i)
        delete machines[i];
    delete[] machines;

    for (int i = 0; i < denomCount; ++i)
        delete denoms[i].count;
    delete[] denoms;

    return 0;
}

The main() function starts the ATM program by setting up the available cash notes (10 notes each of $100, $50, $20, and $10),
then, it creates two dispensers: one using the greedy method and the other using the optimal method. 
The program asks the user to enter the amount they want to withdraw, then tries to dispense that amount using both dispensers, showing the results.
Finally, it frees all the memory used before ending.



