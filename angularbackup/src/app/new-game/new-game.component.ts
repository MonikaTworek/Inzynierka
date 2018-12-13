import { Component, OnInit } from '@angular/core';
import {TableService} from '../table.service';
import {ConnectToBlackJackService} from '../connect-to-black-jack.service';
import {Visibility} from 'tslint/lib/rules/completedDocsRule';
import {Router} from '@angular/router';

@Component({
  selector: 'app-new-game',
  templateUrl: './new-game.component.html',
  styleUrls: ['./new-game.component.scss']
})
export class NewGameComponent implements OnInit {
  game_over: any;
  new_game: any;

  constructor(private server: ConnectToBlackJackService, private table: TableService, private router: Router) { }

  ngOnInit() {
    this.game_over.visibility = false;
    this.new_game.visibility = false;
  }

  New_Game() {
    this.server.BeginGame().subscribe(begin => {
        this.table.SetRow1(begin.croupier.hand.cards);
        this.table.SetRow2(begin.player.hands1.cards);
        this.table.SetRow3(begin.player.hands2.cards);
      }
    );
    this.new_game.visibility = false;
  }

  Visibility(tekst) {
    if (tekst.header === 'error' && tekst.message === 'You finish') {
      this.game_over.visibility = true;
    }

    if (tekst.phase === 'end_game') {
      this.new_game.visibility = true;
    }
  }

  Score() {
    this.router.navigate(['/game']);
  }
}
