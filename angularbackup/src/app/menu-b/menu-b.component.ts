import { Component, OnInit } from '@angular/core';
import {ConnectToBlackJackService} from '../connect-to-black-jack.service';
import {TableService} from '../table.service';
import {Router} from '@angular/router';
import {WynikDanychComponent} from '../wynik-danych/wynik-danych.component';
import {WynikGraczaComponent} from '../wynik-gracza/wynik-gracza.component';
import {NewGameComponent} from '../new-game/new-game.component';

@Component({
  selector: 'app-menu-b',
  templateUrl: './menu-b.component.html',
  styleUrls: ['./menu-b.component.scss']
})
export class MenuBComponent implements OnInit {

  constructor(private server: ConnectToBlackJackService, private table: TableService, private router: Router, private  newG: NewGameComponent,
              private  score: WynikDanychComponent, private  playercsore: WynikGraczaComponent) { }

  ngOnInit() {
  }
// new game -> okienko kto wygral, a na klikniecie ok nowa gra
  Hit1() {
    this.server.Hit1().subscribe(begin => {
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow2(begin.player.hands1.cards);
      this.newG.Visibility(begin);
    });
  }

  Hit2() {
    this.server.Hit2().subscribe(begin => {
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow3(begin.player.hands2.cards);
      this.newG.Visibility(begin);
    });
  }

  Stand1() {
    this.server.Stand1().subscribe( begin => {
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow2(begin.player.hands1.cards);
      this.table.SetRow3(begin.player.hands2.cards);
      this.newG.Visibility(begin);
    });
  }

  Stand2() {
    this.server.Stand2().subscribe( begin => {
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow2(begin.player.hands1.cards);
      this.table.SetRow3(begin.player.hands2.cards);
      this.newG.Visibility(begin);
    });
  }

  Double_down() {
    this.server.Double_down().subscribe(begin => {
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow2(begin.player.hands1.cards);
      this.table.SetRow3(begin.player.hands2.cards);
      this.newG.Visibility(begin);
    });
  }

  Split() {
    this.server.Split().subscribe(begin => {
      this.table.SetRow1(begin.croupier.hand.cards);
      this.table.SetRow2(begin.player.hands1.cards);
      this.table.SetRow3(begin.player.hands2.cards);
      this.newG.Visibility(begin);
    });
  }

  Insure() {
    this.server.Insure();
  }

  Surrender() {
    this.server.Surrender();
  }

  End_game() {
    this.server.End_game();
    this.server.Finish_game().subscribe(end =>{
      this.score.Update(end);
      this.playercsore.Update(end);
    });
    this.router.navigate(['/solution']);
  }
}
