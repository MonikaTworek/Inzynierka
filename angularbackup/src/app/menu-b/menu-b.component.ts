import { Component, OnInit } from '@angular/core';
import {ConnectToBlackJackService} from '../connect-to-black-jack.service';
import {TableService} from '../table.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-menu-b',
  templateUrl: './menu-b.component.html',
  styleUrls: ['./menu-b.component.scss']
})
export class MenuBComponent implements OnInit {
  game_over: any;
  new_game: any;
  status: any;
  zawartosc: any;
  new_game_fun: any;

  constructor(private server: ConnectToBlackJackService, private table: TableService, private router: Router) { }

  ngOnInit() {
    this.game_over  = false;
    if (this.server.GetFirst()) {
      this.new_game = true;
      if (this.server.GetWin() === 'Croupier') {
        this.zawartosc = 'PRZEGRAŁEŚ';
      }
      if (this.server.GetWin() === 'Player') {
        this.zawartosc = 'WYGRAŁEŚ';
      }
      if (this.server.GetWin() === 'Draw') {
        this.zawartosc = 'REMIS';
      }
      this.status = true;
      this.new_game_fun = true;
    } else {
      this.new_game = false;
      this.status = false;
      this.new_game_fun = false;
    }
  }
  // BEGIN GAME -> CO JAK OCZKO?!?!?!?!?!

  Visibility(tekst: any) {
    this.status = true;
    if (String(tekst.phase) === 'end_game') {
      this.zawartosc = '';
      if (tekst.player.hands1.winner === 'Croupier' || tekst.player.hands2.winner === 'Croupier') {
        this.zawartosc = 'PRZEGRAŁEŚ';
      }
      if (tekst.player.hands1.winner === 'Player' || tekst.player.hands2.winner === 'Player') {
        this.zawartosc += ' WYGRAŁEŚ';
      }
      if (tekst.player.hands1.winner === 'Draw' || tekst.player.hands2.winner === 'Draw') {
        this.zawartosc += ' REMIS';
      }
      this.new_game = true;
      this.new_game_fun = true;
    }
  }

  New_Game() {
    this.server.BeginGame().subscribe((begin: any) => {
      if (begin.end_game) {
        this.game_over = true;
        return;
      }
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow2(begin.player.hands1.cards);
      this.table.SetRow3(begin.player.hands2.cards);
      this.Visibility(begin);
    });
    this.new_game = false;
    this.new_game_fun = false;
    this.status = false;
  }

  Hit1() {
    this.server.Hit1().subscribe((begin: any) => {
      if (begin.end_game) {
        this.game_over = true;
        return;
      }
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow2(begin.player.hands1.cards);
      this.Visibility(begin);
    });
  }

  Hit2() {
    this.server.Hit2().subscribe((begin: any) => {
      if (begin.end_game) {
        this.game_over = true;
        return;
      }
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow3(begin.player.hands2.cards);
      this.Visibility(begin);
    });
  }

  Stand1() {
    this.server.Stand1().subscribe( (begin: any) => {
      if (begin.end_game) {
        this.game_over = true;
        return;
      }
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow2(begin.player.hands1.cards);
      this.table.SetRow3(begin.player.hands2.cards);
      this.Visibility(begin);
    });
  }

  Stand2() {
    this.server.Stand2().subscribe( (begin: any) => {
      if (begin.end_game) {
        this.game_over = true;
        return;
      }
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow2(begin.player.hands1.cards);
      this.table.SetRow3(begin.player.hands2.cards);
      this.Visibility(begin);
    });
  }

  Double_down() {
    this.server.Double_down().subscribe((begin: any) => {
      if (begin.end_game) {
        this.game_over = true;
        return;
      }
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow2(begin.player.hands1.cards);
      this.table.SetRow3(begin.player.hands2.cards);
      this.Visibility(begin);
    });
  }

  Split() {
    this.server.Split().subscribe((begin: any) => {
      if (begin.end_game) {
        this.game_over = true;
        return;
      }
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow2(begin.player.hands1.cards);
      this.table.SetRow3(begin.player.hands2.cards);
      this.Visibility(begin);
    });
  }

  Insure() {
    this.server.Insure();
  }

  Surrender() {
    this.server.Surrender().subscribe( (begin: any) => {
      if (begin.end_game) {
        this.game_over = true;
        return;
      }
      this.Visibility(begin);
    });
  }

  End_game() {
    this.server.End_game();
    this.server.Finish_game().subscribe((end: any) => {
      this.server.Update(end);
    });
    this.router.navigate(['/solution']);
  }
}
