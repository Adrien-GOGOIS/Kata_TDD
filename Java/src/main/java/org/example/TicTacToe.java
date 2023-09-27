package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class TicTacToe {
    private static List<String> state;

    public TicTacToe() {
        state = new ArrayList<>(9);
        state.add(" ");
        state.add(" ");
        state.add(" ");
        state.add(" ");
        state.add(" ");
        state.add(" ");
        state.add(" ");
        state.add(" ");
        state.add(" ");
    }

    public void play(String playerSymbol, int position) {
        if (!Objects.equals(state.get(position), " ")) {
            throw new IllegalArgumentException("This case is not empty");
        } else {
            state.add(position, playerSymbol);
        }
    }

    public String getList(int position) {
        return state.get(position);
    }

    public void printGame() {
        StringBuilder lines = new StringBuilder();
        for (int index = 0; index < 9; index++) {
            lines.append(String.format("[ %s ] ", state.get(index)));
            if (index == 2 || index == 5) {
                lines.append("\n");
            }
        }
        System.out.println(lines);
    }
}
