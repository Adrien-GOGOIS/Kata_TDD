package org.exemple;

import org.assertj.core.api.Assertions;
import org.example.TicTacToe;
import org.junit.jupiter.api.Test;

public class TicTacToeTest {

    TicTacToe game = new TicTacToe();
    Player player1 = new Player("X");
    Player player2 = new Player("O");

    @Test
    void should_start_game_with_empty_cells() {
        Assertions.assertThat(game.getList(3)).isEqualTo(" ");
    }

    @Test
    void should_accept_any_case_at_game_beginning() {
        player1.play(1, game);
        Assertions.assertThat(game.getList(1)).isEqualTo("X");
    }

    @Test
    void should_not_accept_already_played_case() {
        player2.play(1, game);
        Assertions.assertThatThrownBy(() -> {
                    player2.play(1, game);
                }).isInstanceOf(IllegalArgumentException.class)
                .hasMessageContaining("This case is not empty");
    }

    @Test
    void should_player_1_win_the_game() {
        player1.play(0, game);
        player1.play(1, game);
        player1.play(2, game);
        Assertions.assertThat(player1.isWinner(game)).isTrue();
    }

    @Test
    void should_player_1_do_not_win_the_game() {
        player1.play(0, game);
        player1.play(2, game);
        Assertions.assertThat(player1.isWinner(game)).isFalse();
    }
}
