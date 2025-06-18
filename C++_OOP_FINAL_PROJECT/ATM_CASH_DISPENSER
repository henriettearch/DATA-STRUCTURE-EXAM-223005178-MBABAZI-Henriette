#include <iostream>  // Includes input/output functionality
#include <algorithm> // Includes algorithms like sort()

using namespace std; // Allows using standard names without 'std::'

// Define a structure to represent a currency denomination
struct Denomination {
    int value;      // The value of the note (e.g., 100, 50)
    int* count;     // Pointer to the number of such notes available
};

// Global pointer to array of denominations
Denomination* denoms = nullptr;
// Count of how many denominations exist
int denomCount = 0;

// Function to add a new denomination dynamically
void addDenomination(int value, int count) {
    // Check if this denomination already exists
    for (int i = 0; i < denomCount; ++i) {
        if ((denoms + i)->value == value) {
            *(denoms[i].count) += count; // If it exists, just increase the count
            return;
        }
    }

    // Create a new array to hold one more denomination
    Denomination* newArr = new Denomination[denomCount + 1];
    // Copy old denominations to new array
    for (int i = 0; i < denomCount; ++i)
        *(newArr + i) = *(denoms + i);

    // Add new denomination to the end
    newArr[denomCount].value = value;
    newArr[denomCount].count = new int(count);

    // Delete old array and update global pointer
    delete[] denoms;
    denoms = newArr;
    ++denomCount; // Increase the count of denominations
}

// Function to remove a denomination by its value
void removeDenomination(int value) {
    int index = -1;
    // Find the index of the denomination to remove
    for (int i = 0; i < denomCount; ++i) {
        if ((denoms + i)->value == value) {
            index = i;
            break;
        }
    }
    if (index == -1) return; // Not found, do nothing

    // Create a new array for remaining denominations
    Denomination* newArr = new Denomination[denomCount - 1];
    for (int i = 0, j = 0; i < denomCount; ++i) {
        if (i == index) {
            delete denoms[i].count; // Free memory for removed denomination
            continue;
        }
        *(newArr + j++) = *(denoms + i); // Copy remaining items
    }
    delete[] denoms;
    denoms = newArr;
    --denomCount; // Decrease the count
}

// Abstract class for a cash dispenser
class CashDispenser {
public:
    virtual bool dispense(int amount) = 0; // Pure virtual function
    virtual ~CashDispenser() {} // Virtual destructor
};

// Greedy strategy: give out largest notes first
class GreedyDispenser : public CashDispenser {
public:
    bool dispense(int amount) override {
        cout << "\n[Greedy Dispenser] Dispensing $" << amount << "...\n";
        int* temp = new int[denomCount]; // Backup original note counts
        for (int i = 0; i < denomCount; ++i) temp[i] = *(denoms + i)->count;

        // Sort denominations in descending order
        sort(denoms, denoms + denomCount, [](const Denomination& a, const Denomination& b) {
            return a.value > b.value;
        });

        int remaining = amount; // Amount left to give
        for (int i = 0; i < denomCount && remaining > 0; ++i) {
            Denomination* d = denoms + i;
            int num = min(*(d->count), remaining / d->value); // Max notes possible
            remaining -= num * d->value; // Reduce remaining amount
            *(d->count) -= num; // Decrease note count
            if (num > 0)
                cout << "Dispensed " << num << " x $" << d->value << "\n";
        }

        // If not fully dispensed, restore original note counts
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
};

// Optimal strategy: use fewest notes (brute-force)
class OptimalDispenser : public CashDispenser {
public:
    bool dispense(int amount) override {
        cout << "\n[Optimal Dispenser] Dispensing $" << amount << " (minimal notes)...\n";
        int minNotes = INT_MAX; // Track fewest notes used
        int* bestUsed = new int[denomCount]{}; // Best note combination
        bool found = false;

        // Start recursive backtracking search
        backtrack(0, amount, 0, new int[denomCount]{}, bestUsed, minNotes, found);

        if (!found) {
            cout << "Unable to dispense full amount.\n";
            delete[] bestUsed;
            return false;
        }

        // Dispense the best found combination
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
    // Recursive function to try all combinations of notes
    void backtrack(int idx, int remaining, int usedNotes, int* used,
                   int* bestUsed, int& minNotes, bool& found) {
        if (remaining == 0) { // Found valid solution
            if (usedNotes < minNotes) {
                for (int i = 0; i < denomCount; ++i)
                    bestUsed[i] = used[i]; // Save this as best so far
                minNotes = usedNotes;
                found = true;
            }
            return;
        }

        if (idx >= denomCount) return; // End of denominations

        Denomination* d = denoms + idx;
        int maxUse = min(*(d->count), remaining / d->value); // Max notes we can use
        for (int i = maxUse; i >= 0; --i) {
            used[idx] = i;
            backtrack(idx + 1, remaining - i * d->value, usedNotes + i, used, bestUsed, minNotes, found);
        }
        used[idx] = 0; // Reset
    }
};

int main() {
    cout << "=== ATM Cash Dispenser ===\n";

    // Add different denominations with initial counts
    addDenomination(100, 10);
    addDenomination(50, 10);
    addDenomination(20, 10);
    addDenomination(10, 10);

    // Create an array of cash dispenser machines
    int machineCount = 2;
    CashDispenser** machines = new CashDispenser*[machineCount];
    machines[0] = new GreedyDispenser(); // First is greedy strategy
    machines[1] = new OptimalDispenser(); // Second is optimal strategy

    // Ask user how much they want to withdraw
    int amount;
    cout << "\nEnter amount to dispense: ";
    cin >> amount;

    // Try dispensing using both machines
    for (int i = 0; i < machineCount; ++i) {
        machines[i]->dispense(amount);
        cout << "-----------------------------\n";
    }

    // Clean up memory for machines
    for (int i = 0; i < machineCount; ++i)
        delete machines[i];
    delete[] machines;

    // Clean up memory for denominations
    for (int i = 0; i < denomCount; ++i)
        delete denoms[i].count;
    delete[] denoms;

    return 0; // End of program
}
