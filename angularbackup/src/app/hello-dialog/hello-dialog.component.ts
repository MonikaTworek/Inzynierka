import { Component, OnInit } from '@angular/core';
import {ConnectToBlackJackService} from '../connect-to-black-jack.service';
import {TableService} from '../table.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-hello-dialog',
  templateUrl: './hello-dialog.component.html',
  styleUrls: ['./hello-dialog.component.scss']
})
export class HelloDialogComponent implements OnInit {
  numberOfCards: number;

  constructor(private server: ConnectToBlackJackService, private table: TableService, private router: Router) {
  }

  ngOnInit() {
  }

  Register() {
    console.log(this.numberOfCards);
    this.server.Register(this.numberOfCards).subscribe((register: any) => {
      this.server.RememberID(register.uid);
      this.server.BeginGame().subscribe((begin: any) => {
          this.table.SetRow1(begin.croupier.hand.cards);
          this.table.SetRow2(begin.player.hands1.cards);
          this.router.navigate(['/game']);
          if (begin.phase === 'end_game') {
            this.server.SetFirst(true, begin.player.winner);
          } else {
            this.server.SetFirst(false, 'None');
          }
        }
      );
    });
  }

  Generate() {
    this.server.GenerateData(this.numberOfCards).subscribe( (lol: any) => {
      this.GoTo(lol);
    });
    // jezeli header to sukces to/generate, a jak nie to /badgenerate
  }

  GoTo (tekst: any) {
    if (tekst.header === 'success') {
      this.router.navigate(['/generate']);
    } else {
      this.router.navigate(['/bad_generate']);
    }
  }


  ReadMe() {
    this.router.navigate(['/readme']);
  }
}
