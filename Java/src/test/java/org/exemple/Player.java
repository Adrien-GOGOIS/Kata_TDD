package org.exemple;

import org.example.TicTacToe;

import java.util.Objects;

public class Player {

    String symbol;

    public Player(String symbol) {
        this.symbol = symbol;
    }

    public void play(int position, TicTacToe game) {
        game.play(symbol, position);
    }

    public boolean isWinner(TicTacToe game) {
        return Objects.equals(game.getList(0), symbol) &&
                Objects.equals(game.getList(1), symbol) &&
                Objects.equals(game.getList(2), symbol);
    }
}
